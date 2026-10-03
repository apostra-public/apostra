import asyncio
import json
import os
import unittest
from pathlib import Path
from threading import Event
from unittest.mock import patch

import httpx

from apostra import Apostra, ApostraError, AsyncApostra, InFlightReceiptError, ProtocolError, RateLimitError, get_handoff, m2m_token_provider, m2m_token_provider_async, open_handoff, paginate, paginate_async, poll, settle, settle_async
from apostra._version import __version__
from apostra.models import SaveCatalogInput
from apostra.transport import OPERATIONS


def sdk_manifest_path() -> Path:
    repository = Path(__file__).parents[3]
    private_path = repository / 'scripts/codegen/apostra-sdk/manifest.json'
    if private_path.is_file():
        return private_path
    return repository / 'sdk/release/manifest.json'


class TransportTests(unittest.TestCase):
    def test_m2m_provider_caches_and_refreshes_without_authorization_header(self) -> None:
        requests: list[httpx.Request] = []

        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(
                200,
                json={
                    'access_token': f'token-{len(requests)}',
                    'expires_in': 120 if len(requests) == 1 else 60,
                },
            )

        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            provider = m2m_token_provider(
                client_id='client',
                client_secret='secret',
                scope=['interchange:read', 'interchange:write'],
                http_client=http,
            )
            self.assertEqual(provider(), 'token-1')
            self.assertEqual(provider(), 'token-1')
            expiring_provider = m2m_token_provider(
                client_id='client',
                client_secret='secret',
                scope='interchange:read',
                http_client=http,
            )
            self.assertEqual(expiring_provider(), 'token-2')
            self.assertEqual(expiring_provider(), 'token-3')
        self.assertEqual(len(requests), 3)
        self.assertEqual(str(requests[0].url), 'https://identity.scope3.com/oauth2/token')
        self.assertNotIn('authorization', requests[0].headers)
        self.assertEqual(
            requests[0].content,
            b'client_id=client&client_secret=secret&grant_type=client_credentials&scope=interchange%3Aread+interchange%3Awrite',
        )

    def test_m2m_provider_does_not_expose_a_secret_in_failures(self) -> None:
        with httpx.Client(transport=httpx.MockTransport(lambda _request: httpx.Response(401, text='secret-value'))) as http:
            provider = m2m_token_provider(client_id='client', client_secret='secret-value', scope='interchange:read', http_client=http)
            with self.assertRaisesRegex(ValueError, 'M2M token request failed') as raised:
                provider()
        self.assertNotIn('secret-value', str(raised.exception))
    def test_environment_defaults_allow_zero_config_status_and_explicit_overrides(self) -> None:
        requests: list[httpx.Request] = []

        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={'data': {}, 'error': None})

        with patch.dict(os.environ, {
            'APOSTRA_API_KEY': 'environment-key',
            'APOSTRA_ACCOUNT_ID': '12',
            'APOSTRA_BASE_URL': 'https://environment.example',
        }):
            with httpx.Client(transport=httpx.MockTransport(handle)) as http:
                Apostra(http_client=http).get_status()
                Apostra(
                    access_token='explicit-token',
                    account_id='34',
                    base_url='https://explicit.example',
                    http_client=http,
                ).get_status()
            with self.assertRaisesRegex(ValueError, 'Use HTTPS'):
                with patch.dict(os.environ, {'APOSTRA_BASE_URL': 'http://not-loopback.example'}):
                    Apostra()

        self.assertEqual(str(requests[0].url), 'https://environment.example/tools/get_status')
        self.assertEqual(requests[0].headers['authorization'], 'Bearer environment-key')
        self.assertEqual(requests[0].headers['X-SCOPE3-CUSTOMER-ID'], '12')
        self.assertEqual(str(requests[1].url), 'https://explicit.example/tools/get_status')
        self.assertEqual(requests[1].headers['authorization'], 'Bearer explicit-token')
        self.assertEqual(requests[1].headers['X-SCOPE3-CUSTOMER-ID'], '34')

    def test_unauthorized_does_not_replay_or_refresh_implicitly(self) -> None:
        tokens = iter(['expired', 'fresh'])
        requests: list[httpx.Request] = []
        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            if request.headers['authorization'] == 'Bearer expired':
                return httpx.Response(401, json={'data': None, 'error': {'code': 'UNAUTHORIZED', 'message': 'expired'}})
            return httpx.Response(200, json={'data': {}, 'error': None})
        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            api = Apostra(token_provider=lambda: next(tokens), http_client=http)
            with self.assertRaises(ApostraError) as raised:
                api.get_status({})
            self.assertEqual(raised.exception.status, 401)
            self.assertEqual(len(requests), 1)
            api.get_status({})
            self.assertEqual(requests[1].headers['authorization'], 'Bearer fresh')

    def test_transient_hinted_4xx_responses_do_not_replay(self) -> None:
        for status in (400, 401, 403):
            requests: list[httpx.Request] = []

            def handle(request: httpx.Request) -> httpx.Response:
                requests.append(request)
                return httpx.Response(status, json={'data': None, 'error': {'code': 'REQUEST_REJECTED', 'message': 'do not replay', 'recovery': 'transient'}})

            with httpx.Client(transport=httpx.MockTransport(handle)) as http:
                with self.assertRaises(ApostraError) as raised:
                    Apostra(api_key='key', http_client=http).get_status({})
            self.assertEqual(raised.exception.status, status)
            self.assertTrue(raised.exception.retryable)
            self.assertEqual(len(requests), 1)

    def test_explicit_retry_preserves_idempotency_key_and_account(self) -> None:
        requests: list[httpx.Request] = []
        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(429, json={'data': None, 'error': {'code': 'RATE_LIMITED', 'message': 'try later'}})
        input: SaveCatalogInput = {'catalogId': 'catalog-1', 'advertiserId': '123', 'name': 'Example', 'type': 'product', 'items': [], 'idempotencyKey': 'original-key'}
        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            api = Apostra(api_key='key', account_id='12', max_retries=0, http_client=http)
            for count in (1, 2):
                with self.assertRaises(ApostraError) as raised:
                    api.save_catalog(input, idempotency_key='original-key')
                self.assertEqual(raised.exception.status, 429)
                self.assertIsInstance(raised.exception, RateLimitError)
                self.assertEqual(raised.exception.code, 'RATE_LIMITED')
                self.assertEqual(raised.exception.recovery, 'transient')
                self.assertTrue(raised.exception.retryable)
                self.assertEqual(len(requests), count)
        self.assertEqual(requests[0].content, requests[1].content)
        self.assertEqual(json.loads(requests[1].content)['idempotencyKey'], 'original-key')
        self.assertEqual(requests[1].headers['X-SCOPE3-CUSTOMER-ID'], '12')
        self.assertEqual(requests[1].headers['idempotency-key'], 'original-key')

    def test_write_requires_a_caller_supplied_idempotency_key_before_dispatch(self) -> None:
        requests: list[httpx.Request] = []

        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={'data': {}, 'error': None})

        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            with self.assertRaises(ValueError):
                Apostra(api_key='key', http_client=http).save_ask(
                    {'id': 'ask-1', 'requesterState': 'accepted'},
                    idempotency_key='',
                )
        self.assertEqual(requests, [])

    def test_retries_transient_reads_and_caller_keyed_writes(self) -> None:
        requests: list[httpx.Request] = []

        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            if len(requests) in {1, 3}:
                return httpx.Response(503, json={'data': None, 'error': {'code': 'UNAVAILABLE', 'message': 'later'}})
            return httpx.Response(200, json={'data': {}, 'error': None})

        with patch('apostra.transport.random.uniform', return_value=0):
            with httpx.Client(transport=httpx.MockTransport(handle)) as http:
                api = Apostra(api_key='key', http_client=http)
                self.assertEqual(api.get_status({}), {})
                self.assertEqual(
                    api.save_ask(
                        {'id': 'ask-1', 'requesterState': 'accepted'},
                        idempotency_key='ask-1',
                    ),
                    {},
                )
        self.assertEqual(len(requests), 4)
        self.assertEqual(requests[2].content, requests[3].content)
        self.assertEqual(requests[3].headers['idempotency-key'], 'ask-1')

    def test_retry_after_sets_a_lower_bound_for_full_jitter(self) -> None:
        calls = 0

        def handle(_request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            if calls == 1:
                return httpx.Response(429, json={'data': None, 'error': {'code': 'RATE_LIMITED', 'message': 'later', 'retry_after': 1}})
            return httpx.Response(200, json={'data': {}, 'error': None})

        with patch('apostra.transport.random.uniform', return_value=0.25):
            with patch('apostra.transport._wait') as wait:
                with httpx.Client(transport=httpx.MockTransport(handle)) as http:
                    self.assertEqual(Apostra(api_key='key', http_client=http).get_status({}), {})
        self.assertEqual(wait.call_args.args[0], 1)

    def test_settle_reuses_the_caller_operation_until_complete(self) -> None:
        calls = 0

        def run() -> dict[str, bool]:
            nonlocal calls
            calls += 1
            if calls == 1:
                raise InFlightReceiptError(
                    'r1',
                    0,
                    {'id': '4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1', 'state': 'running', 'stateVersion': 1, 'stateChangedAt': '2026-09-28T10:00:00.000Z'},
                )
            return {'done': True}

        self.assertEqual(settle(run, timeout=1), {'done': True})
        self.assertEqual(calls, 2)

    def test_local_validation_precedes_credentials(self) -> None:
        calls: list[bool] = []
        def token() -> str:
            calls.append(True)
            return 'key'
        with Apostra(token_provider=token) as api:
            with self.assertRaises(ValueError):
                api.get_status({}, timeout=0)
            with self.assertRaises(ValueError):
                api.get_status({}, account_id='0')
        self.assertEqual(calls, [])

    def test_error_envelope_requires_data(self) -> None:
        with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(401, json={'error': {'code': 'UNAUTHORIZED', 'message': 'expired'}}))) as http:
            with self.assertRaises(ProtocolError):
                Apostra(api_key='key', http_client=http).get_status({})

    def test_success_credentials_accounts_and_wire(self) -> None:
        requests: list[httpx.Request] = []
        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={'data': {}, 'error': None})
        tokens = iter(['token-1', 'token-2'])
        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            api = Apostra(token_provider=lambda: next(tokens), account_id='12', http_client=http)
            api.get_status({})
            api.get_status({}, account_id='34')
            self.assertEqual(requests[0].headers['authorization'], 'Bearer token-1')
            self.assertEqual(requests[1].headers['X-SCOPE3-CUSTOMER-ID'], '34')
            self.assertEqual(requests[1].headers['user-agent'], f'apostra-python/{__version__}')
            self.assertEqual(json.loads(requests[0].content), {})
            api.close()
            self.assertFalse(http.is_closed)
            self.assertNotIn('token-', repr(api))

    def test_generated_response_method_exposes_success_metadata(self) -> None:
        with httpx.Client(
            transport=httpx.MockTransport(
                lambda _request: httpx.Response(
                    200,
                    json={'data': {'ready': True}, 'error': None},
                    headers={'x-request-id': 'request-1'},
                )
            )
        ) as http:
            response = Apostra(api_key='key', http_client=http).get_status_with_response({})
        self.assertEqual(response['data'], {'ready': True})
        self.assertEqual(response['request_id'], 'request-1')
        self.assertEqual(response['headers']['x-request-id'], 'request-1')

    def test_body_idempotency_key_matches_header(self) -> None:
        requests: list[httpx.Request] = []
        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={'data': {}, 'error': None})
        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            api = Apostra(api_key='key', http_client=http)
            api.request_buyer_child_account({'parentId': '1', 'name': 'Buyer'}, idempotency_key='request-1')
            self.assertEqual(requests[0].headers['idempotency-key'], 'request-1')
            self.assertEqual(json.loads(requests[0].content)['idempotencyKey'], 'request-1')
            api.request_buyer_child_account({'parentId': '1', 'name': 'Buyer', 'idempotencyKey': 'request-1'}, idempotency_key='request-1')
            self.assertEqual(json.loads(requests[1].content)['idempotencyKey'], 'request-1')
            with self.assertRaisesRegex(ValueError, 'idempotencyKey must match'):
                api.request_buyer_child_account({'parentId': '1', 'name': 'Buyer', 'idempotencyKey': 'other'}, idempotency_key='request-1')
            self.assertEqual(len(requests), 2)

    def test_typed_failure_no_retry_or_secret_in_string(self) -> None:
        calls = 0
        def handle(request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            return httpx.Response(429, json={'data': None, 'error': {'code': 'RATE_LIMITED', 'message': 'secret', 'retry_after': 12, 'recovery': 'transient'}}, headers={'x-request-id': 'r1'})
        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            api = Apostra(api_key='secret-key', max_retries=0, http_client=http)
            with self.assertRaises(ApostraError) as raised:
                api.get_status({})
            self.assertEqual(raised.exception.error.get('retry_after'), 12)
            self.assertEqual(raised.exception.request_id, 'r1')
            self.assertNotIn('secret', str(raised.exception))
            self.assertEqual(calls, 1)

    def test_sync_token_provider_cannot_extend_the_request_deadline(self) -> None:
        calls = 0
        started = Event()
        release = Event()
        requests: list[httpx.Request] = []

        def token() -> str:
            nonlocal calls
            calls += 1
            started.set()
            release.wait()
            return 'key'

        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            raise AssertionError('Timed-out token acquisition must not dispatch HTTP')

        try:
            with httpx.Client(transport=httpx.MockTransport(handle)) as http:
                api = Apostra(token_provider=token, timeout=0.01, http_client=http)
                with self.assertRaises(TimeoutError):
                    api.get_status({})
                self.assertTrue(started.wait(0.1))
                with self.assertRaises(TimeoutError):
                    api.get_status({})
            self.assertEqual(requests, [])
            self.assertEqual(calls, 1)
        finally:
            release.set()

    def test_sync_token_and_http_share_one_request_deadline(self) -> None:
        observed: list[float] = []

        def handle(request: httpx.Request) -> httpx.Response:
            observed.append(request.extensions['timeout']['connect'])
            return httpx.Response(200, json={'data': {}, 'error': None})

        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            with patch('apostra.transport.monotonic', side_effect=[100, 103, 103, 103]):
                Apostra(token_provider=lambda: 'key', timeout=5, http_client=http).get_status({})
        self.assertEqual(observed, [2])

    def test_sync_http_cannot_extend_the_request_deadline(self) -> None:
        calls = 0
        started = Event()
        release = Event()

        def handle(_request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            started.set()
            release.wait()
            return httpx.Response(200, json={'data': {}, 'error': None})

        try:
            with httpx.Client(transport=httpx.MockTransport(handle)) as http:
                api = Apostra(api_key='key', timeout=0.01, http_client=http)
                with self.assertRaises(TimeoutError):
                    api.get_status({})
                self.assertTrue(started.wait(0.1))
                with self.assertRaises(TimeoutError):
                    api.get_status({})
            self.assertEqual(calls, 1)
        finally:
            release.set()

    def test_inflight_receipt_is_not_a_completed_result_or_an_automatic_retry(self) -> None:
        calls = 0
        def handle(request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            return httpx.Response(202, json={'data': {'receipt': {'id': '4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1', 'state': 'uncertain', 'stateVersion': 2, 'stateChangedAt': '2026-09-28T10:00:00.000Z'}}, 'error': None}, headers={'retry-after': '3', 'x-request-id': 'r1'})
        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            with self.assertRaises(InFlightReceiptError) as raised:
                Apostra(api_key='key', http_client=http).save_ask(
                    {'id': 'ask-1', 'requesterState': 'accepted'},
                    idempotency_key='ask-1',
                )
        self.assertEqual(raised.exception.status, 202)
        self.assertEqual(raised.exception.request_id, 'r1')
        self.assertEqual(raised.exception.retry_after, 3)
        self.assertEqual(raised.exception.receipt['state'], 'uncertain')
        self.assertEqual(raised.exception.receipt['stateVersion'], 2)
        self.assertEqual(calls, 1)

    def test_malformed_response_and_redirect(self) -> None:
        for response in (httpx.Response(200, json={'data': {}}), httpx.Response(502, text='secret'), httpx.Response(302, headers={'location': 'https://elsewhere.test'})):
            with httpx.Client(transport=httpx.MockTransport(lambda request: response)) as http:
                with self.assertRaises(ProtocolError):
                    Apostra(api_key='key', http_client=http).get_status({})

    def test_binary_documents(self) -> None:
        def handle(request: httpx.Request) -> httpx.Response:
            self.assertIn(b'a%2Fb', request.url.raw_path)
            return httpx.Response(200, content=b'document')
        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            self.assertEqual(Apostra(access_token='m2m', http_client=http).download_v3_public_document_revision({'documentId':'a/b','revisionId':'v1'}), b'document')

    def test_parity(self) -> None:
        import re
        manifest = json.loads(sdk_manifest_path().read_text())
        self.assertEqual(sorted(OPERATIONS), sorted(manifest['operations']))
        for name in OPERATIONS:
            method = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
            self.assertTrue(callable(getattr(Apostra, method)))
            self.assertTrue(callable(getattr(AsyncApostra, method)))
            self.assertTrue(callable(getattr(Apostra, f'{method}_with_response')))
            self.assertTrue(callable(getattr(AsyncApostra, f'{method}_with_response')))

    def test_pagination(self) -> None:
        self.assertEqual(list(paginate(lambda cursor: {'next': None if cursor else 'next'}, lambda page: page['next'])), [{'next':'next'}, {'next':None}])
        with self.assertRaises(ProtocolError):
            list(paginate(lambda cursor: 'same', lambda page: page))
        repeated = paginate(lambda cursor: 'same', lambda page: page)
        self.assertEqual(next(repeated), 'same')
        with self.assertRaises(ProtocolError):
            next(repeated)

    def test_headless_handoff(self) -> None:
        handoff = get_handoff({
            'humanHandoff': {
                'kind': 'human_action_required',
                'url': 'https://example.test/task',
                'expiresAt': '2026-10-01T00:05:00.000Z',
                'resume': {
                    'kind': 'manual',
                    'reason': 'This Page has no durable completion receipt. Read the affected object before continuing; opening or closing the browser is not completion.',
                },
            },
        })
        self.assertIsNotNone(handoff)
        if handoff is None:
            self.fail('Expected a human handoff')
        self.assertEqual(open_handoff(handoff), 'https://example.test/task')
        self.assertIsNone(get_handoff({'humanHandoff': {'kind': 'human_action_unavailable'}}))
        self.assertIsNone(get_handoff({
            'humanHandoff': {
                'kind': 'human_action_required',
                'url': 'https://example.test/task',
                'expiresAt': '2026-10-01T00:05:00.000Z',
                'resume': {},
            },
        }))
        with self.assertRaises(ValueError):
            open_handoff('javascript:alert(1)')


class AsyncTests(unittest.IsolatedAsyncioTestCase):
    async def test_generated_response_method_exposes_success_metadata(self) -> None:
        async with httpx.AsyncClient(
            transport=httpx.MockTransport(
                lambda _request: httpx.Response(
                    200,
                    json={'data': {'ready': True}, 'error': None},
                    headers={'x-request-id': 'request-1'},
                )
            )
        ) as http:
            response = await AsyncApostra(
                api_key='key', http_client=http
            ).get_status_with_response({})
        self.assertEqual(response['data'], {'ready': True})
        self.assertEqual(response['request_id'], 'request-1')
        self.assertEqual(response['headers']['x-request-id'], 'request-1')

    async def test_async_m2m_provider_coalesces_concurrent_refreshes(self) -> None:
        requests: list[httpx.Request] = []

        async def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            await asyncio.sleep(0)
            return httpx.Response(200, json={'access_token': 'token-1', 'expires_in': 120})

        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
            provider = m2m_token_provider_async(client_id='client', client_secret='secret', scope='interchange:read', http_client=http)
            self.assertEqual(await asyncio.gather(provider(), provider()), ['token-1', 'token-1'])
        self.assertEqual(len(requests), 1)

    async def test_async_environment_defaults_allow_zero_config_status(self) -> None:
        requests: list[httpx.Request] = []

        async def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={'data': {}, 'error': None})

        with patch.dict(os.environ, {
            'APOSTRA_API_KEY': 'environment-key',
            'APOSTRA_ACCOUNT_ID': '12',
            'APOSTRA_BASE_URL': 'https://environment.example',
        }):
            async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
                await AsyncApostra(http_client=http).get_status()

        self.assertEqual(str(requests[0].url), 'https://environment.example/tools/get_status')
        self.assertEqual(requests[0].headers['authorization'], 'Bearer environment-key')
        self.assertEqual(requests[0].headers['X-SCOPE3-CUSTOMER-ID'], '12')

    async def test_async_body_idempotency_key_matches_header(self) -> None:
        requests: list[httpx.Request] = []
        async def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={'data': {}, 'error': None})
        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
            api = AsyncApostra(api_key='key', http_client=http)
            await api.request_buyer_child_account({'parentId': '1', 'name': 'Buyer'}, idempotency_key='request-1')
            self.assertEqual(requests[0].headers['idempotency-key'], 'request-1')
            self.assertEqual(json.loads(requests[0].content)['idempotencyKey'], 'request-1')
            await api.request_buyer_child_account({'parentId': '1', 'name': 'Buyer', 'idempotencyKey': 'request-1'}, idempotency_key='request-1')
            self.assertEqual(json.loads(requests[1].content)['idempotencyKey'], 'request-1')
            with self.assertRaisesRegex(ValueError, 'idempotencyKey must match'):
                await api.request_buyer_child_account({'parentId': '1', 'name': 'Buyer', 'idempotencyKey': 'other'}, idempotency_key='request-1')
            self.assertEqual(len(requests), 2)

    async def test_async_pagination_cursor_cycle(self) -> None:
        cursors: list[str | None] = []
        async def read(cursor: str | None) -> str:
            cursors.append(cursor)
            return 'same'
        with self.assertRaises(ProtocolError):
            async for _page in paginate_async(read, lambda page: page):
                pass
        self.assertEqual(cursors, [None, 'same'])

    async def test_helper_cancellation_reaches_pending_reads(self) -> None:
        for kind in ('poll', 'paginate'):
            entered = asyncio.Event()
            stopped = asyncio.Event()
            async def read(cursor: str | None = None) -> int:
                entered.set()
                try:
                    await asyncio.Event().wait()
                    return 0
                finally:
                    stopped.set()
            async def consume() -> None:
                async for _page in paginate_async(read, lambda page: 'next'):
                    pass
            task = asyncio.create_task(poll(read, lambda value: False, timeout=1)) if kind == 'poll' else asyncio.create_task(consume())
            await entered.wait()
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            self.assertTrue(stopped.is_set())

    async def test_poll_propagates_failure_without_retry(self) -> None:
        calls = 0
        async def read() -> int:
            nonlocal calls
            calls += 1
            raise RuntimeError('read failed')
        with self.assertRaisesRegex(RuntimeError, 'read failed'):
            await poll(read, lambda value: False, timeout=1)
        self.assertEqual(calls, 1)

    async def test_async_auth_failure_does_not_replay(self) -> None:
        calls: list[httpx.Request] = []
        tokens: list[bool] = []
        async def token() -> str:
            tokens.append(True)
            return 'access-token'
        async def handle(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            return httpx.Response(401, json={'data': None, 'error': {'code': 'UNAUTHORIZED', 'message': 'expired'}})
        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
            api = AsyncApostra(token_provider=token, account_id='12', http_client=http)
            with self.assertRaises(ApostraError) as raised:
                await api.get_status({})
            self.assertEqual(raised.exception.status, 401)
            self.assertEqual(len(tokens), 1)
            self.assertEqual(len(calls), 1)
            self.assertEqual(calls[0].headers['authorization'], 'Bearer access-token')
            self.assertEqual(calls[0].headers['X-SCOPE3-CUSTOMER-ID'], '12')
            with self.assertRaises(ValueError):
                await api.get_status({}, account_id='0')
            self.assertEqual(len(tokens), 1)

    async def test_async_success(self) -> None:
        async def token() -> str:
            return 'token'
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda request: httpx.Response(200, json={'data': {}, 'error': None}))) as http:
            async with AsyncApostra(token_provider=token, http_client=http) as api:
                self.assertEqual(await api.get_status({}), {})
            self.assertFalse(http.is_closed)

    async def test_async_retries_transient_reads_and_settles_receipts(self) -> None:
        calls = 0

        async def handle(_request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            if calls == 1:
                return httpx.Response(503, json={'data': None, 'error': {'code': 'UNAVAILABLE', 'message': 'later'}})
            return httpx.Response(200, json={'data': {}, 'error': None})

        with patch('apostra.transport.random.uniform', return_value=0):
            async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
                self.assertEqual(await AsyncApostra(api_key='key', http_client=http).get_status({}), {})

        settle_calls = 0

        async def run() -> dict[str, bool]:
            nonlocal settle_calls
            settle_calls += 1
            if settle_calls == 1:
                raise InFlightReceiptError(
                    'r1',
                    0,
                    {'id': '4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1', 'state': 'running', 'stateVersion': 1, 'stateChangedAt': '2026-09-28T10:00:00.000Z'},
                )
            return {'done': True}

        self.assertEqual(await settle_async(run, timeout=1), {'done': True})
        self.assertEqual(calls, 2)
        self.assertEqual(settle_calls, 2)

    async def test_cancel_inflight_and_provider(self) -> None:
        async def token() -> str:
            await asyncio.sleep(100)
            return 'token'
        async with AsyncApostra(token_provider=token) as api:
            with self.assertRaises(TimeoutError):
                await api.get_status({}, timeout=0.001)
        async def handle(request: httpx.Request) -> httpx.Response:
            await asyncio.sleep(100)
            return httpx.Response(200)
        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
            task = asyncio.create_task(AsyncApostra(api_key='key', http_client=http).get_status({}))
            await asyncio.sleep(0)
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task

    async def test_poll_timeout(self) -> None:
        async def read() -> int:
            return 1
        self.assertEqual(await poll(read, lambda value: value == 1, timeout=1), 1)
        with self.assertRaises(TimeoutError):
            await poll(read, lambda value: False, timeout=0.001)
