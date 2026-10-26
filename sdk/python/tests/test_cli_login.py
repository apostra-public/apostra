import asyncio
import json
import os
import stat
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from datetime import UTC, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from apostra import Apostra, AsyncApostra, cli_login
from apostra.cli_login import (
    CliLoginEntry,
    cli_login_lock,
    cli_login_token_provider,
    credentials_path,
    normalize_base_url,
    read_cli_login,
    refresh_cli_login,
    write_cli_login,
)
from apostra.transport import TimeoutError as ApostraTimeoutError


def iso(offset: timedelta) -> str:
    moment = datetime.now(UTC) + offset
    return moment.isoformat(timespec="milliseconds").replace("+00:00", "Z")


class FakeServer:
    """A local authorization server and V3 API. Never production."""

    def __init__(self) -> None:
        self.refresh_requests = 0
        self.refresh_forms: list[dict[str, list[str]]] = []
        self.api_tokens: list[str] = []
        self.refresh_status = 200
        self.omit_refresh_token = False
        self.refresh_delay = 0.1
        self._count = threading.Lock()
        fake = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, format: str, *args: Any) -> None:
                pass

            def reply(self, status: int, body: object) -> None:
                payload = json.dumps(body).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def do_GET(self) -> None:
                path = urlsplit(self.path).path
                if path == "/.well-known/oauth-authorization-server":
                    return self.reply(
                        200,
                        {
                            "issuer": fake.origin,
                            "authorization_endpoint": f"{fake.origin}/authorize",
                            "token_endpoint": f"{fake.origin}/auth/token",
                        },
                    )
                if path == "/api/v3/tools/get_status":
                    fake.api_tokens.append(self.headers.get("Authorization", ""))
                    self.api_headers = dict(self.headers)
                    return self.reply(
                        200, {"data": {"account": {"accountId": 7}}, "error": None}
                    )
                self.reply(404, {})

            def do_POST(self) -> None:
                path = urlsplit(self.path).path
                if path == "/api/v3/tools/get_status":
                    return self.do_GET()
                length = int(self.headers.get("Content-Length", "0"))
                form = parse_qs(self.rfile.read(length).decode())
                if path != "/auth/token" or form.get("resource") != [fake.resource]:
                    return self.reply(400, {"error": "invalid_target"})
                with fake._count:
                    fake.refresh_requests += 1
                    number = fake.refresh_requests
                    fake.refresh_forms.append(form)
                time.sleep(fake.refresh_delay)
                if fake.refresh_status != 200:
                    return self.reply(fake.refresh_status, {"error": "invalid_grant"})
                self.reply(
                    200,
                    {
                        "access_token": f"at-{number}",
                        **(
                            {}
                            if fake.omit_refresh_token
                            else {"refresh_token": f"rt-{number}"}
                        ),
                        "expires_in": 3600,
                        "scope": "interchange:read",
                    },
                )

        self._server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self._server.daemon_threads = True
        self.origin = f"http://127.0.0.1:{self._server.server_address[1]}"
        self.resource = f"{self.origin}/api/v3"
        threading.Thread(
            target=self._server.serve_forever, args=(0.01,), daemon=True
        ).start()

    def entry(self, **over: Any) -> CliLoginEntry:
        entry: dict[str, Any] = {
            "issuer": self.origin,
            "resource": self.resource,
            "clientId": f"{self.origin}/oauth/clients/apostra-cli.json",
            "accessToken": "at-0",
            "refreshToken": "rt-0",
            "expiresAt": iso(timedelta(seconds=-1)),
            "accountId": "7",
            "scopes": ["interchange:read"],
            **over,
        }
        return entry  # type: ignore[return-value]

    def close(self) -> None:
        self._server.shutdown()
        self._server.server_close()


class LoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.dir = Path(directory.name)
        environment = patch.dict(
            os.environ,
            {"XDG_CONFIG_HOME": directory.name, "APPDATA": directory.name},
        )
        environment.start()
        self.addCleanup(environment.stop)
        for name in ("APOSTRA_API_KEY", "APOSTRA_ACCOUNT_ID", "APOSTRA_BASE_URL"):
            os.environ.pop(name, None)
        self.fake = FakeServer()
        self.addCleanup(self.fake.close)

    def store(self, **over: Any) -> None:
        with cli_login_lock():
            write_cli_login(self.fake.resource, self.fake.entry(**over))

    def fresh(self) -> None:
        self.store(expiresAt=iso(timedelta(hours=1)))


class StoreTests(LoginTestCase):
    @unittest.skipIf(sys.platform == "win32", "POSIX file modes")
    def test_writes_atomically_with_private_modes_keyed_per_base_url(self) -> None:
        self.store()
        path = credentials_path()
        self.assertEqual(path, self.dir / "apostra" / "credentials.json")
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
        self.assertEqual(stat.S_IMODE(path.parent.stat().st_mode), 0o700)
        self.assertEqual(
            [p.name for p in path.parent.iterdir() if p.name.endswith(".tmp")], []
        )
        written = json.loads(path.read_text())
        self.assertEqual(written["version"], 1)
        self.assertEqual(list(written["logins"]), [self.fake.resource])
        with cli_login_lock():
            write_cli_login("https://other.example/api/v3", self.fake.entry())
        self.assertIsNotNone(read_cli_login(self.fake.resource + "/"))
        self.assertIsNotNone(read_cli_login("https://other.example/api/v3"))

    def test_corrupt_or_incomplete_file_is_no_login(self) -> None:
        self.assertIsNone(read_cli_login(self.fake.resource))
        credentials_path().parent.mkdir(parents=True)
        credentials_path().write_text("{not json")
        self.assertIsNone(read_cli_login(self.fake.resource))
        credentials_path().write_text(
            json.dumps({"logins": {self.fake.resource: {"accessToken": "x"}}})
        )
        self.assertIsNone(read_cli_login(self.fake.resource))

    def test_base_url_keys_match_the_cli(self) -> None:
        for raw, key in {
            "https://api.apostra.com/api/v3": "https://api.apostra.com/api/v3",
            "https://API.apostra.com/api/v3/": "https://api.apostra.com/api/v3",
            "https://api.apostra.com": "https://api.apostra.com",
            "https://api.apostra.com:443/api/v3": "https://api.apostra.com/api/v3",
            "http://127.0.0.1:8080/api/v3": "http://127.0.0.1:8080/api/v3",
            "http://localhost": "http://localhost",
            "http://[::1]:3000/x": "http://[::1]:3000/x",
        }.items():
            self.assertEqual(normalize_base_url(raw), key)
        for bad in (
            "http://example.com",
            "https://user:pw@example.com",
            "https://example.com/api?x=1",
            "https://example.com/#frag",
            "not a url",
        ):
            with self.assertRaises(ValueError, msg=bad):
                normalize_base_url(bad)

    def test_unknown_fields_and_other_logins_survive_a_refresh(self) -> None:
        self.store(extra="kept")
        with cli_login_lock():
            write_cli_login("https://other.example/api/v3", self.fake.entry())
        refresh_cli_login(self.fake.resource)
        logins = json.loads(credentials_path().read_text())["logins"]
        self.assertEqual(logins[self.fake.resource]["extra"], "kept")
        self.assertEqual(logins[self.fake.resource]["accessToken"], "at-1")
        self.assertIn("https://other.example/api/v3", logins)


class RefreshTests(LoginTestCase):
    def test_rotates_the_refresh_token_and_writes_it_back(self) -> None:
        self.store()
        entry = refresh_cli_login(self.fake.resource)
        self.assertEqual(entry["accessToken"], "at-1")
        stored = read_cli_login(self.fake.resource)
        assert stored is not None
        self.assertEqual(stored["refreshToken"], "rt-1")
        self.assertEqual(stored["accountId"], "7")
        self.assertTrue(stored["expiresAt"].endswith("Z"))
        form = self.fake.refresh_forms[0]
        self.assertEqual(form["grant_type"], ["refresh_token"])
        self.assertEqual(form["refresh_token"], ["rt-0"])
        self.assertEqual(form["client_id"], [self.fake.entry()["clientId"]])
        self.assertEqual(form["resource"], [self.fake.resource])

    def test_a_fresh_login_makes_no_request(self) -> None:
        self.fresh()
        self.assertEqual(refresh_cli_login(self.fake.resource)["accessToken"], "at-0")
        self.assertEqual(self.fake.refresh_requests, 0)

    def test_keeps_the_old_refresh_token_when_the_server_does_not_rotate(self) -> None:
        self.store()
        self.fake.omit_refresh_token = True
        refresh_cli_login(self.fake.resource)
        stored = read_cli_login(self.fake.resource)
        assert stored is not None
        self.assertEqual(stored["refreshToken"], "rt-0")
        self.assertEqual(stored["accessToken"], "at-1")

    def test_a_revoked_login_says_to_sign_in_again_without_echoing_anything(
        self,
    ) -> None:
        self.store()
        self.fake.refresh_status = 400
        with self.assertRaises(ValueError) as raised:
            refresh_cli_login(self.fake.resource)
        self.assertIn("Run `apostra login` again", str(raised.exception))
        self.assertNotIn("rt-0", str(raised.exception))
        stored = read_cli_login(self.fake.resource)
        assert stored is not None
        self.assertEqual(stored["refreshToken"], "rt-0")

    def test_no_login_says_to_sign_in(self) -> None:
        with self.assertRaisesRegex(ValueError, "Not signed in to .* `apostra login`"):
            refresh_cli_login(self.fake.resource)

    def test_discovery_uses_the_stored_issuer_and_refuses_a_mismatch(self) -> None:
        self.store(issuer="http://127.0.0.1:1")
        with self.assertRaises(Exception) as raised:
            refresh_cli_login(self.fake.resource)
        self.assertEqual(self.fake.refresh_requests, 0)
        self.assertNotIn("rt-0", str(raised.exception))
        self.store(issuer="https://not-the-issuer.example")
        with self.assertRaises(Exception):
            refresh_cli_login(self.fake.resource)
        self.assertEqual(self.fake.refresh_requests, 0)

    def test_concurrent_threads_make_exactly_one_token_request(self) -> None:
        self.store()
        providers = [
            cli_login_token_provider(base_url=self.fake.resource) for _ in range(3)
        ]
        tokens: list[str] = []

        def call(index: int) -> None:
            tokens.append(providers[index % 3]())

        threads = [threading.Thread(target=call, args=(i,)) for i in range(6)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(tokens, ["at-1"] * 6)
        self.assertEqual(self.fake.refresh_requests, 1)

    def test_concurrent_processes_make_exactly_one_token_request(self) -> None:
        self.store()
        script = (
            "import sys\n"
            "from apostra.cli_login import cli_login_token_provider\n"
            "print(cli_login_token_provider(base_url=sys.argv[1])())\n"
        )
        processes = [
            subprocess.Popen(
                [sys.executable, "-I", "-c", script, self.fake.resource],
                stdout=subprocess.PIPE,
                text=True,
            )
            for _ in range(3)
        ]
        outputs = [p.communicate(timeout=60)[0].strip() for p in processes]
        self.assertEqual([p.returncode for p in processes], [0, 0, 0])
        self.assertEqual(outputs, ["at-1"] * 3)
        self.assertEqual(self.fake.refresh_requests, 1)


class LockTests(LoginTestCase):
    def lock_path(self) -> Path:
        return Path(f"{credentials_path()}.lock")

    def test_the_lock_file_holds_an_owner_token_and_is_removed_on_exit(self) -> None:
        with cli_login_lock():
            owner = self.lock_path().read_text()
            self.assertRegex(owner, r"^\d+:[0-9a-f-]{36}$")
            self.assertEqual(stat.S_IMODE(self.lock_path().stat().st_mode), 0o600)
        self.assertFalse(self.lock_path().exists())

    def test_never_removes_a_lock_another_process_owns(self) -> None:
        with cli_login_lock():
            self.lock_path().write_text("another-owner")
        self.assertEqual(self.lock_path().read_text(), "another-owner")

    def test_breaks_a_stale_lock_left_by_a_dead_process(self) -> None:
        self.store()
        self.lock_path().write_text("")
        old = time.time() - 60
        os.utime(self.lock_path(), (old, old))
        self.assertEqual(refresh_cli_login(self.fake.resource)["accessToken"], "at-1")

    def test_takeover_leaves_no_guard_behind(self) -> None:
        self.lock_path().parent.mkdir(parents=True)
        self.lock_path().write_text("dead-owner")
        old = time.time() - 60
        os.utime(self.lock_path(), (old, old))
        with cli_login_lock():
            self.assertNotEqual(self.lock_path().read_text(), "dead-owner")
        self.assertFalse(Path(f"{self.lock_path()}.takeover").exists())

    def test_a_takeover_that_lost_the_race_leaves_the_new_lock_alone(self) -> None:
        self.lock_path().parent.mkdir(parents=True)
        self.lock_path().write_text("new-owner")
        cli_login.break_stale_lock(self.lock_path())
        self.assertEqual(self.lock_path().read_text(), "new-owner")
        self.assertFalse(Path(f"{self.lock_path()}.takeover").exists())

    def test_a_live_takeover_guard_blocks_a_second_waiter(self) -> None:
        self.lock_path().parent.mkdir(parents=True)
        self.lock_path().write_text("dead-owner")
        guard = Path(f"{self.lock_path()}.takeover")
        guard.write_text("")
        old = time.time() - 60
        os.utime(self.lock_path(), (old, old))
        with patch.object(cli_login, "_LOCK_WAIT_S", 0.2):
            with self.assertRaises(ApostraTimeoutError):
                with cli_login_lock():
                    self.fail("broke a lock while another waiter held the guard")
        self.assertEqual(self.lock_path().read_text(), "dead-owner")

    def test_a_guard_left_by_a_crashed_process_goes_stale(self) -> None:
        self.lock_path().parent.mkdir(parents=True)
        self.lock_path().write_text("dead-owner")
        guard = Path(f"{self.lock_path()}.takeover")
        guard.write_text("")
        old = time.time() - 60
        os.utime(self.lock_path(), (old, old))
        os.utime(guard, (old, old))
        with cli_login_lock():
            pass
        self.assertFalse(guard.exists())

    def test_waiters_racing_over_a_stale_lock_never_overlap(self) -> None:
        self.lock_path().parent.mkdir(parents=True)
        self.lock_path().write_text("dead-owner")
        old = time.time() - 60
        os.utime(self.lock_path(), (old, old))
        inside = 0
        overlaps = 0
        guard = threading.Lock()

        def work() -> None:
            nonlocal inside, overlaps
            for _ in range(10):
                with cli_login_lock():
                    with guard:
                        inside += 1
                        overlaps += inside > 1
                    time.sleep(0.002)
                    with guard:
                        inside -= 1

        threads = [threading.Thread(target=work) for _ in range(8)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(overlaps, 0)

    def test_waits_for_a_live_lock_then_gives_up(self) -> None:
        self.lock_path().parent.mkdir(parents=True)
        self.lock_path().write_text("another-owner")
        with patch.object(cli_login, "_LOCK_WAIT_S", 0.2):
            with self.assertRaisesRegex(ApostraTimeoutError, "another Apostra login"):
                with cli_login_lock():
                    self.fail("took a lock another process holds")
        self.assertEqual(self.lock_path().read_text(), "another-owner")

    def test_a_heartbeat_keeps_a_long_held_lock_from_going_stale(self) -> None:
        with patch.object(cli_login, "_LOCK_HEARTBEAT_S", 0.05):
            with cli_login_lock():
                old = time.time() - 20
                os.utime(self.lock_path(), (old, old))
                time.sleep(0.4)
                self.assertLess(time.time() - self.lock_path().stat().st_mtime, 5)

    def test_a_heartbeat_does_not_touch_a_lock_another_process_owns(self) -> None:
        with patch.object(cli_login, "_LOCK_HEARTBEAT_S", 0.05):
            with cli_login_lock():
                self.lock_path().write_text("another-owner")
                old = time.time() - 20
                os.utime(self.lock_path(), (old, old))
                time.sleep(0.3)
                self.assertGreater(time.time() - self.lock_path().stat().st_mtime, 15)


class CredentialChainTests(LoginTestCase):
    def test_explicit_credential_beats_everything(self) -> None:
        self.fresh()
        os.environ["APOSTRA_API_KEY"] = "env-key"
        Apostra(base_url=self.fake.resource, api_key="explicit-key").get_status()
        Apostra(base_url=self.fake.resource, access_token="explicit-token").get_status()
        Apostra(base_url=self.fake.resource, token_provider=lambda: "p").get_status()
        self.assertEqual(
            self.fake.api_tokens,
            ["Bearer explicit-key", "Bearer explicit-token", "Bearer p"],
        )

    def test_environment_api_key_beats_the_login(self) -> None:
        self.fresh()
        os.environ["APOSTRA_API_KEY"] = "env-key"
        Apostra(base_url=self.fake.resource).get_status()
        self.assertEqual(self.fake.api_tokens, ["Bearer env-key"])

    def test_uses_the_login_when_nothing_else_is_set(self) -> None:
        self.fresh()
        with Apostra(base_url=self.fake.resource) as api:
            api.get_status()
        self.assertEqual(self.fake.api_tokens, ["Bearer at-0"])

    def test_base_url_comes_from_the_environment(self) -> None:
        self.fresh()
        os.environ["APOSTRA_BASE_URL"] = self.fake.resource
        Apostra().get_status()
        self.assertEqual(self.fake.api_tokens, ["Bearer at-0"])

    def test_refreshes_an_expired_login_transparently(self) -> None:
        self.store()
        Apostra(base_url=self.fake.resource).get_status()
        self.assertEqual(self.fake.api_tokens, ["Bearer at-1"])
        self.assertEqual(self.fake.refresh_requests, 1)

    def test_no_credential_and_no_login_keeps_the_existing_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "Supply exactly one of api_key"):
            Apostra(base_url=self.fake.resource)

    def test_ignores_a_login_stored_for_a_different_base_url(self) -> None:
        self.fresh()
        with self.assertRaisesRegex(ValueError, "Supply exactly one"):
            Apostra(base_url="https://elsewhere.example/api/v3")

    def test_an_invalid_base_url_keeps_its_own_error_with_a_login_stored(self) -> None:
        self.fresh()
        with self.assertRaisesRegex(ValueError, "Supply exactly one"):
            Apostra(base_url="http://example.com")

    def test_refuses_an_explicit_account_that_differs_from_the_login(self) -> None:
        self.fresh()
        with self.assertRaisesRegex(ValueError, "does not match account 7"):
            Apostra(base_url=self.fake.resource, account_id="8")
        os.environ["APOSTRA_ACCOUNT_ID"] = "9"
        with self.assertRaisesRegex(ValueError, "does not match account 7"):
            Apostra(base_url=self.fake.resource)
        del os.environ["APOSTRA_ACCOUNT_ID"]
        api = Apostra(base_url=self.fake.resource, account_id="7")
        api.get_status()
        self.assertEqual(self.fake.api_tokens, ["Bearer at-0"])

    def test_an_explicit_credential_skips_the_account_check(self) -> None:
        self.fresh()
        Apostra(base_url=self.fake.resource, api_key="key", account_id="8")

    def test_a_logout_after_construction_says_to_sign_in(self) -> None:
        self.store()
        api = Apostra(base_url=self.fake.resource)
        credentials_path().unlink()
        with self.assertRaisesRegex(ValueError, "Not signed in"):
            api.get_status()


class AsyncCredentialChainTests(LoginTestCase, unittest.IsolatedAsyncioTestCase):
    async def test_async_client_uses_and_refreshes_the_login_once(self) -> None:
        self.store()
        async with AsyncApostra(base_url=self.fake.resource) as api:
            await asyncio.gather(api.get_status(), api.get_status(), api.get_status())
        self.assertEqual(self.fake.api_tokens, ["Bearer at-1"] * 3)
        self.assertEqual(self.fake.refresh_requests, 1)

    async def test_async_client_refuses_a_different_account(self) -> None:
        self.fresh()
        with self.assertRaisesRegex(ValueError, "does not match account 7"):
            AsyncApostra(base_url=self.fake.resource, account_id="8")


if __name__ == "__main__":
    unittest.main()
