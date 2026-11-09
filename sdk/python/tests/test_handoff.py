import asyncio
import json
import unittest
from collections.abc import Mapping
from threading import Event, Timer
from typing import Any, cast

import httpx

from apostra import Apostra, AsyncApostra, Handoff, InFlightReceiptError, find_handoff
from apostra.models import GetResult
from apostra.transport import TimeoutError as ApostraTimeoutError

URL = "https://app.example.com/handoff/abc"
EXPIRES = "2026-11-10T00:00:00.000Z"

RECEIPT = cast(
    Any,
    {
        "id": "4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1",
        "operation": "save_ask",
        "state": "running",
        "stateVersion": 1,
        "stateChangedAt": "2026-09-28T10:00:00.000Z",
        "pendingReason": "The write is still being processed.",
    },
)


def connection_resume(intended: str | None = "conn_1") -> dict[str, object]:
    return {
        "kind": "connection",
        "targetKind": "gam",
        "targetId": "target_1",
        "intendedConnectionId": intended,
        "correlationId": "corr_1",
    }


def manual_result(**overrides: object) -> dict[str, object]:
    handoff: dict[str, object] = {
        "kind": "human_action_required",
        "account": {"id": 42, "name": "Acme"},
        "action": "connect_provider",
        "url": URL,
        "expiresAt": EXPIRES,
        "resume": {"kind": "manual", "reason": "Finish setup in the browser"},
    }
    handoff.update(overrides)
    return {"humanHandoff": handoff}


def approval_result(state: str = "pending", **overrides: object) -> dict[str, object]:
    approval: dict[str, object] = {
        "id": "appr_1",
        "kind": "iu_plan.accept",
        "state": state,
        "url": URL,
        "expiresAt": EXPIRES,
        "targetCustomerId": "77",
    }
    approval.update(overrides)
    return {"action": "approval_required", "approval": approval}


def handoff_of(result: Mapping[str, object]) -> Handoff:
    handoff = find_handoff(result)
    if handoff is None:
        raise AssertionError("expected a handoff")
    return handoff


def in_flight() -> InFlightReceiptError:
    return InFlightReceiptError("r1", 0, RECEIPT)


class Script:
    """Reads that return or raise each scripted step in order."""

    def __init__(self, *steps: object) -> None:
        self.steps = list(steps)
        self.calls = 0
        self.timeouts: list[float] = []

    def _next(self) -> object:
        step = self.steps[min(self.calls, len(self.steps) - 1)]
        self.calls += 1
        if isinstance(step, BaseException):
            raise step
        return step

    def read(self, timeout: float) -> dict[str, object]:
        self.timeouts.append(timeout)
        return cast(dict[str, object], self._next())

    async def read_async(self) -> dict[str, object]:
        return cast(dict[str, object], self._next())


def done_flag(result: dict[str, object]) -> bool:
    return result.get("done") is True


class FindHandoffTests(unittest.TestCase):
    def test_normalises_a_manual_human_handoff(self) -> None:
        handoff = handoff_of(manual_result())
        self.assertEqual(handoff.kind, "human_action_required")
        self.assertEqual(handoff.url, URL)
        self.assertEqual(handoff.account, {"id": "42", "name": "Acme"})
        self.assertEqual(handoff.action, "connect_provider")
        self.assertEqual(handoff.expires_at, EXPIRES)
        self.assertEqual(
            handoff.resume,
            {"kind": "manual", "reason": "Finish setup in the browser"},
        )

    def test_normalises_a_connection_human_handoff(self) -> None:
        self.assertEqual(
            handoff_of(manual_result(resume=connection_resume())).resume,
            connection_resume(),
        )
        self.assertEqual(
            handoff_of(manual_result(resume=connection_resume(None))).resume,
            connection_resume(None),
        )

    def test_normalises_an_approval_required_result(self) -> None:
        handoff = handoff_of(approval_result("executing"))
        self.assertEqual(handoff.kind, "approval_required")
        self.assertEqual(handoff.url, URL)
        self.assertEqual(handoff.account, {"id": "77", "name": None})
        self.assertEqual(handoff.action, "iu_plan.accept")
        self.assertEqual(handoff.expires_at, EXPIRES)
        self.assertEqual(
            handoff.resume,
            {"kind": "approval", "approvalId": "appr_1", "state": "executing"},
        )

    def test_accepts_every_approval_state(self) -> None:
        for state in ("pending", "executing", "succeeded", "failed", "rejected", "expired"):
            with self.subTest(state=state):
                resume = handoff_of(approval_result(state)).resume
                self.assertEqual(resume["kind"], "approval")
                self.assertEqual(cast(dict[str, object], resume)["state"], state)

    def test_returns_none_when_nothing_is_asked_of_a_person(self) -> None:
        self.assertIsNone(find_handoff(None))
        self.assertIsNone(find_handoff({}))
        self.assertIsNone(find_handoff({"action": "saved", "id": 1}))
        self.assertIsNone(find_handoff({"humanHandoff": "nope"}))
        self.assertIsNone(find_handoff({"action": "approval_required"}))

    def test_returns_none_for_human_action_unavailable(self) -> None:
        self.assertIsNone(find_handoff(manual_result(kind="human_action_unavailable")))

    def test_returns_none_for_a_malformed_human_handoff(self) -> None:
        bad_connection_id = {**connection_resume(), "intendedConnectionId": 5}
        no_correlation = {k: v for k, v in connection_resume().items() if k != "correlationId"}
        cases: dict[str, dict[str, object]] = {
            "empty url": {"url": ""},
            "missing url": {"url": None},
            "missing expiresAt": {"expiresAt": None},
            "missing action": {"action": None},
            "missing account": {"account": None},
            "zero account id": {"account": {"id": 0, "name": "Acme"}},
            "negative account id": {"account": {"id": -1, "name": "Acme"}},
            "string account id": {"account": {"id": "42", "name": "Acme"}},
            "boolean account id": {"account": {"id": True, "name": "Acme"}},
            "float account id": {"account": {"id": 1.5, "name": "Acme"}},
            "missing account name": {"account": {"id": 42}},
            "missing resume": {"resume": None},
            "unknown resume kind": {"resume": {"kind": "poll"}},
            "manual without reason": {"resume": {"kind": "manual"}},
            "connection without correlation id": {"resume": no_correlation},
            "connection with non-string connection id": {"resume": bad_connection_id},
        }
        for name, overrides in cases.items():
            with self.subTest(name):
                self.assertIsNone(find_handoff(manual_result(**overrides)))

    def test_returns_none_for_an_unknown_approval_state(self) -> None:
        self.assertIsNone(find_handoff(approval_result("cancelled")))

    def test_returns_none_for_an_approval_missing_a_field(self) -> None:
        for field in ("id", "kind", "url", "expiresAt", "targetCustomerId"):
            with self.subTest(field):
                result = approval_result()
                cast(dict[str, object], result["approval"])[field] = None
                self.assertIsNone(find_handoff(result))


class OpenTests(unittest.TestCase):
    def test_headless_open_returns_the_url(self) -> None:
        self.assertEqual(handoff_of(manual_result()).open(), URL)

    def test_open_calls_the_opener_and_returns_the_url(self) -> None:
        opened: list[str] = []
        self.assertEqual(handoff_of(manual_result()).open(opened.append), URL)
        self.assertEqual(opened, [URL])

    def test_open_rejects_a_non_https_url_without_calling_the_opener(self) -> None:
        opened: list[str] = []
        handoff = handoff_of(manual_result(url="http://app.example.com/handoff"))
        with self.assertRaises(ValueError):
            handoff.open(opened.append)
        self.assertEqual(opened, [])


class WaitForCompletionTests(unittest.TestCase):
    def test_polls_an_approval_until_it_leaves_pending_and_executing(self) -> None:
        final: dict[str, object] = {"saved": True}
        script = Script(approval_result("pending"), approval_result("executing"), final)
        result = handoff_of(approval_result()).wait_for_completion(
            read=script.read, timeout=5, interval=0.001
        )
        self.assertIs(result, final)
        self.assertEqual(script.calls, 3)

    def test_each_read_receives_the_seconds_left(self) -> None:
        script = Script(approval_result("pending"), approval_result("pending"), {"saved": True})
        handoff_of(approval_result()).wait_for_completion(
            read=script.read, timeout=5, interval=0.001
        )
        self.assertEqual(len(script.timeouts), 3)
        for left in script.timeouts:
            self.assertGreater(left, 0)
            self.assertLessEqual(left, 5)
        self.assertEqual(script.timeouts, sorted(script.timeouts, reverse=True))

    def test_a_rejected_approval_read_is_done(self) -> None:
        rejected = approval_result("rejected")
        script = Script(approval_result("pending"), rejected)
        result = handoff_of(approval_result()).wait_for_completion(
            read=script.read, timeout=5, interval=0.001
        )
        self.assertIs(result, rejected)
        self.assertEqual(script.calls, 2)

    def test_reads_once_even_when_the_handoff_already_looks_final(self) -> None:
        fresh = approval_result("succeeded")
        script = Script(fresh)
        result = handoff_of(approval_result("succeeded")).wait_for_completion(
            read=script.read, timeout=5, interval=0.001
        )
        self.assertIs(result, fresh)
        self.assertEqual(script.calls, 1)

    def test_a_caller_until_replaces_the_approval_default(self) -> None:
        script = Script({"done": False}, {"done": True})
        result = handoff_of(approval_result()).wait_for_completion(
            read=script.read, until=done_flag, timeout=5, interval=0.001
        )
        self.assertEqual(result, {"done": True})

    def test_a_manual_handoff_requires_until(self) -> None:
        script = Script({"done": True})
        with self.assertRaises(TypeError):
            handoff_of(manual_result()).wait_for_completion(read=script.read, timeout=5)
        self.assertEqual(script.calls, 0)

    def test_a_manual_handoff_waits_when_until_is_given(self) -> None:
        script = Script({"done": False}, {"done": True})
        result = handoff_of(manual_result()).wait_for_completion(
            read=script.read, until=done_flag, timeout=5, interval=0.001
        )
        self.assertEqual(result, {"done": True})

    def test_an_in_flight_receipt_is_retried(self) -> None:
        final: dict[str, object] = {"saved": True}
        script = Script(in_flight(), final)
        result = handoff_of(approval_result()).wait_for_completion(
            read=script.read, timeout=5, interval=0.001
        )
        self.assertIs(result, final)
        self.assertEqual(script.calls, 2)

    def test_other_read_errors_propagate(self) -> None:
        script = Script(RuntimeError("upstream exploded"))
        with self.assertRaisesRegex(RuntimeError, "upstream exploded"):
            handoff_of(approval_result()).wait_for_completion(
                read=script.read, timeout=5, interval=0.001
            )
        self.assertEqual(script.calls, 1)

    def test_times_out_when_the_step_never_completes(self) -> None:
        script = Script(approval_result("pending"))
        with self.assertRaises(ApostraTimeoutError) as raised:
            handoff_of(approval_result()).wait_for_completion(
                read=script.read, timeout=0.05, interval=0.01
            )
        self.assertIsInstance(raised.exception, TimeoutError)
        self.assertGreaterEqual(script.calls, 1)

    def test_a_set_cancel_event_stops_before_reading(self) -> None:
        cancel = Event()
        cancel.set()
        script = Script(approval_result("pending"))
        with self.assertRaises(asyncio.CancelledError):
            handoff_of(approval_result()).wait_for_completion(
                read=script.read, timeout=5, interval=0.01, cancel=cancel
            )
        self.assertEqual(script.calls, 0)

    def test_cancel_during_the_wait_stops_polling(self) -> None:
        cancel = Event()
        script = Script(approval_result("pending"))
        timer = Timer(0.05, cancel.set)
        timer.start()
        try:
            with self.assertRaises(asyncio.CancelledError):
                handoff_of(approval_result()).wait_for_completion(
                    read=script.read, timeout=5, interval=1, cancel=cancel
                )
        finally:
            timer.cancel()
        self.assertEqual(script.calls, 1)

    def test_invalid_timing_raises_value_error(self) -> None:
        script = Script({"done": True})
        handoff = handoff_of(approval_result())
        bad: list[tuple[float, float]] = [
            (0, 1),
            (-1, 1),
            (float("nan"), 1),
            (float("inf"), 1),
            (5, 0),
            (5, -1),
            (5, float("nan")),
            (5, float("inf")),
        ]
        for timeout, interval in bad:
            with self.subTest(timeout=timeout, interval=interval):
                with self.assertRaises(ValueError):
                    handoff.wait_for_completion(
                        read=script.read, timeout=timeout, interval=interval
                    )
        self.assertEqual(script.calls, 0)


def connection_handoff(intended: str | None = "conn_1") -> Handoff:
    return handoff_of(manual_result(resume=connection_resume(intended)))


def connected(result: GetResult) -> bool:
    return cast(Mapping[str, object], result).get("status") == "connected"


class ClientTests(unittest.TestCase):
    def test_reads_the_named_connection_in_the_handoff_account(self) -> None:
        requests: list[httpx.Request] = []
        statuses = iter(["pending", "connected"])

        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(
                200, json={"data": {"status": next(statuses)}, "error": None}
            )

        with httpx.Client(transport=httpx.MockTransport(handle)) as http:
            api = Apostra(api_key="key", http_client=http)
            result = connection_handoff().wait_for_completion(
                client=api, until=connected, timeout=5, interval=0.001
            )
        self.assertEqual(cast(Mapping[str, object], result)["status"], "connected")
        self.assertEqual(len(requests), 2)
        self.assertTrue(str(requests[0].url).endswith("/tools/get"))
        body = json.loads(requests[0].content)
        self.assertEqual(body["kind"], "connection")
        self.assertEqual(body["id"], "conn_1")
        self.assertEqual(body["accountId"], 42)
        # The get is bounded by the time left, not the client's default.
        read_timeout = cast(Mapping[str, float], requests[0].extensions["timeout"])["read"]
        self.assertLessEqual(read_timeout, 5)

    def test_a_connection_handoff_without_a_connection_id_raises_type_error(self) -> None:
        with httpx.Client(
            transport=httpx.MockTransport(lambda _r: httpx.Response(500))
        ) as http:
            api = Apostra(api_key="key", http_client=http)
            with self.assertRaises(TypeError):
                connection_handoff(None).wait_for_completion(
                    client=api, until=connected, timeout=5
                )

    def test_a_non_connection_handoff_raises_type_error(self) -> None:
        with httpx.Client(
            transport=httpx.MockTransport(lambda _r: httpx.Response(500))
        ) as http:
            api = Apostra(api_key="key", http_client=http)
            for handoff in (handoff_of(manual_result()), handoff_of(approval_result())):
                with self.subTest(kind=handoff.resume["kind"]):
                    with self.assertRaises(TypeError):
                        handoff.wait_for_completion(client=api, until=connected, timeout=5)

    def test_neither_read_nor_client_raises_type_error(self) -> None:
        with self.assertRaises(TypeError):
            cast(Any, handoff_of(approval_result())).wait_for_completion(timeout=5)


class AsyncWaitForCompletionTests(unittest.IsolatedAsyncioTestCase):
    async def test_polls_an_approval_until_it_leaves_pending_and_executing(self) -> None:
        final: dict[str, object] = {"saved": True}
        script = Script(approval_result("pending"), approval_result("executing"), final)
        result = await handoff_of(approval_result()).wait_for_completion_async(
            read=script.read_async, timeout=5, interval=0.001
        )
        self.assertIs(result, final)
        self.assertEqual(script.calls, 3)

    async def test_a_rejected_approval_read_is_done(self) -> None:
        rejected = approval_result("rejected")
        script = Script(approval_result("pending"), rejected)
        result = await handoff_of(approval_result()).wait_for_completion_async(
            read=script.read_async, timeout=5, interval=0.001
        )
        self.assertIs(result, rejected)

    async def test_reads_once_even_when_the_handoff_already_looks_final(self) -> None:
        script = Script(approval_result("succeeded"))
        await handoff_of(approval_result("succeeded")).wait_for_completion_async(
            read=script.read_async, timeout=5, interval=0.001
        )
        self.assertEqual(script.calls, 1)

    async def test_a_manual_handoff_requires_until(self) -> None:
        script = Script({"done": True})
        with self.assertRaises(TypeError):
            await handoff_of(manual_result()).wait_for_completion_async(
                read=script.read_async, timeout=5
            )
        self.assertEqual(script.calls, 0)

    async def test_an_in_flight_receipt_is_retried(self) -> None:
        final: dict[str, object] = {"saved": True}
        script = Script(in_flight(), final)
        result = await handoff_of(approval_result()).wait_for_completion_async(
            read=script.read_async, timeout=5, interval=0.001
        )
        self.assertIs(result, final)
        self.assertEqual(script.calls, 2)

    async def test_other_read_errors_propagate(self) -> None:
        script = Script(RuntimeError("upstream exploded"))
        with self.assertRaisesRegex(RuntimeError, "upstream exploded"):
            await handoff_of(approval_result()).wait_for_completion_async(
                read=script.read_async, timeout=5, interval=0.001
            )

    async def test_times_out_when_the_step_never_completes(self) -> None:
        script = Script(approval_result("pending"))
        with self.assertRaises(TimeoutError):
            await handoff_of(approval_result()).wait_for_completion_async(
                read=script.read_async, timeout=0.05, interval=0.01
            )

    async def test_task_cancellation_stops_polling(self) -> None:
        script = Script(approval_result("pending"))
        task = asyncio.ensure_future(
            handoff_of(approval_result()).wait_for_completion_async(
                read=script.read_async, timeout=5, interval=0.01
            )
        )
        await asyncio.sleep(0.03)
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task

    async def test_invalid_timing_raises_value_error(self) -> None:
        script = Script({"done": True})
        handoff = handoff_of(approval_result())
        with self.assertRaises(ValueError):
            await handoff.wait_for_completion_async(
                read=script.read_async, timeout=0, interval=1
            )
        with self.assertRaises(ValueError):
            await handoff.wait_for_completion_async(
                read=script.read_async, timeout=5, interval=0
            )
        self.assertEqual(script.calls, 0)

    async def test_reads_the_named_connection_in_the_handoff_account(self) -> None:
        requests: list[httpx.Request] = []
        statuses = iter(["pending", "connected"])

        def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(
                200, json={"data": {"status": next(statuses)}, "error": None}
            )

        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
            api = AsyncApostra(api_key="key", http_client=http)
            result = await connection_handoff().wait_for_completion_async(
                client=api, until=connected, timeout=5, interval=0.001
            )
        self.assertEqual(cast(Mapping[str, object], result)["status"], "connected")
        body = json.loads(requests[0].content)
        self.assertEqual(body["kind"], "connection")
        self.assertEqual(body["id"], "conn_1")
        self.assertEqual(body["accountId"], 42)

    async def test_client_type_errors(self) -> None:
        async with httpx.AsyncClient(
            transport=httpx.MockTransport(lambda _r: httpx.Response(500))
        ) as http:
            api = AsyncApostra(api_key="key", http_client=http)
            with self.assertRaises(TypeError):
                await connection_handoff(None).wait_for_completion_async(
                    client=api, until=connected, timeout=5
                )
            with self.assertRaises(TypeError):
                await handoff_of(manual_result()).wait_for_completion_async(
                    client=api, until=connected, timeout=5
                )
            with self.assertRaises(TypeError):
                await cast(Any, handoff_of(approval_result())).wait_for_completion_async(
                    timeout=5
                )


if __name__ == "__main__":
    unittest.main()
