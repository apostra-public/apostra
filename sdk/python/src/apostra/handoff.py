"""One shape for the two ways V3 says "a person must act in a browser".

- A ``humanHandoff`` field: an account-bound, expiring link with a ``resume``
  rule saying how to tell the step is done.
- An ``action: "approval_required"`` result (the web approval contract): the
  request is recorded and runs only after a signed-in person approves it.
  Repeating the original call with the same idempotency key reports the outcome.

Nothing here opens a browser unless the caller asks, and a browser opening or
closing never counts as completion: only a fresh server read does.
"""

from __future__ import annotations

import asyncio
import math
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from threading import Event
from time import monotonic
from typing import TYPE_CHECKING, Literal, TypedDict, TypeVar, cast, get_args, overload

from .transport import InFlightReceiptError, TimeoutError, open_handoff

if TYPE_CHECKING:
    from .client import Apostra, AsyncApostra
    from .models import GetInputKindConnection, GetResult

R = TypeVar("R")

ApprovalState = Literal["pending", "executing", "succeeded", "failed", "rejected", "expired"]


class HandoffAccount(TypedDict):
    id: str
    name: str | None
    """An approval carries no account name."""


class ApprovalResume(TypedDict):
    kind: Literal["approval"]
    approvalId: str
    state: ApprovalState


class ConnectionResume(TypedDict):
    kind: Literal["connection"]
    targetKind: str
    targetId: str
    intendedConnectionId: str | None
    correlationId: str


class ManualResume(TypedDict):
    kind: Literal["manual"]
    reason: str


HandoffResume = ApprovalResume | ConnectionResume | ManualResume


def _text(value: object) -> str | None:
    return value if isinstance(value, str) and value else None


def _approval_waiting(result: object) -> bool:
    if not isinstance(result, Mapping):
        return False
    fields = cast(Mapping[str, object], result)
    approval = fields.get("approval")
    return (
        fields.get("action") == "approval_required"
        and isinstance(approval, Mapping)
        and cast(Mapping[str, object], approval).get("state") in ("pending", "executing")
    )


def _remaining(deadline: float) -> float:
    remaining = deadline - monotonic()
    if remaining <= 0:
        raise TimeoutError("Timed out waiting for the person's step")
    return remaining


def _pause(seconds: float, deadline: float, cancel: Event | None) -> None:
    if (cancel or Event()).wait(min(seconds, _remaining(deadline))):
        raise asyncio.CancelledError()


def _check_timing(timeout: float, interval: float) -> None:
    if (
        not math.isfinite(timeout)
        or not math.isfinite(interval)
        or timeout <= 0
        or interval <= 0
    ):
        raise ValueError("timeout and interval must be positive")


@dataclass(frozen=True)
class Handoff:
    """A step a person must take in a browser, from :func:`find_handoff`."""

    kind: Literal["human_action_required", "approval_required"]
    url: str
    """Sensitive: show it to the person, but do not log or post it."""
    account: HandoffAccount
    action: str
    """The handoff action, or the approval kind such as ``iu_plan.accept``."""
    expires_at: str
    resume: HandoffResume

    def open(self, opener: Callable[[str], object] | None = None) -> str:
        """Open only through the caller's opener; without one, return the URL."""
        return open_handoff(self.url, opener)

    def _until(self, until: Callable[[R], bool] | None) -> Callable[[R], bool]:
        if until is not None:
            return until
        if self.resume["kind"] == "approval":
            return lambda result: not _approval_waiting(result)
        raise TypeError("Pass until: only an approval has a completion rule the SDK knows")

    def _connection_id(self) -> str:
        if self.resume["kind"] != "connection" or self.resume["intendedConnectionId"] is None:
            raise TypeError(
                "client reads only a connection handoff that names its connection; pass read instead"
            )
        return self.resume["intendedConnectionId"]

    @overload
    def wait_for_completion(
        self,
        *,
        read: Callable[[float], R],
        until: Callable[[R], bool] | None = None,
        timeout: float,
        interval: float = 5,
        cancel: Event | None = None,
    ) -> R: ...

    @overload
    def wait_for_completion(
        self,
        *,
        client: Apostra,
        until: Callable[[GetResult], bool],
        timeout: float,
        interval: float = 5,
        cancel: Event | None = None,
    ) -> GetResult: ...

    def wait_for_completion(
        self,
        *,
        read: Callable[[float], R] | None = None,
        client: Apostra | None = None,
        until: Callable[[R], bool] | None = None,
        timeout: float,
        interval: float = 5,
        cancel: Event | None = None,
    ) -> R:
        """Read the server until ``until`` holds, then return that fresh read.

        ``read`` receives the seconds left before ``timeout``; pass them as the
        SDK call's ``timeout`` so a slow read cannot outlast the wait. For an
        approval, ``read`` repeats the original call with the same body and
        idempotency key. ``client`` reads a connection with ``get``.
        """
        _check_timing(timeout, interval)
        if read is None:
            if client is None:
                raise TypeError("Pass read, or client for a connection handoff")
            api = client
            request: GetInputKindConnection = {"kind": "connection", "id": self._connection_id()}

            def read_connection(left: float) -> GetResult:
                return api.get(request, account_id=self.account["id"], timeout=left)

            read = cast(Callable[[float], R], read_connection)
        done = self._until(until)
        deadline = monotonic() + timeout
        while True:
            if cancel and cancel.is_set():
                raise asyncio.CancelledError()
            try:
                result = read(_remaining(deadline))
            except InFlightReceiptError:
                # A keyed write still in flight says nothing about the person's step.
                pass
            else:
                if done(result):
                    return result
            _pause(interval, deadline, cancel)

    @overload
    async def wait_for_completion_async(
        self,
        *,
        read: Callable[[], Awaitable[R]],
        until: Callable[[R], bool] | None = None,
        timeout: float,
        interval: float = 5,
    ) -> R: ...

    @overload
    async def wait_for_completion_async(
        self,
        *,
        client: AsyncApostra,
        until: Callable[[GetResult], bool],
        timeout: float,
        interval: float = 5,
    ) -> GetResult: ...

    async def wait_for_completion_async(
        self,
        *,
        read: Callable[[], Awaitable[R]] | None = None,
        client: AsyncApostra | None = None,
        until: Callable[[R], bool] | None = None,
        timeout: float,
        interval: float = 5,
    ) -> R:
        """Async counterpart to wait_for_completion; task cancellation stops it."""
        _check_timing(timeout, interval)
        if read is None:
            if client is None:
                raise TypeError("Pass read, or client for a connection handoff")
            request: GetInputKindConnection = {"kind": "connection", "id": self._connection_id()}
            read = cast(
                Callable[[], Awaitable[R]],
                lambda: client.get(request, account_id=self.account["id"]),
            )
        done = self._until(until)
        async with asyncio.timeout(timeout):
            while True:
                try:
                    result = await read()
                except InFlightReceiptError:
                    pass
                else:
                    if done(result):
                        return result
                await asyncio.sleep(interval)


def _resume(value: object) -> ConnectionResume | ManualResume | None:
    if not isinstance(value, Mapping):
        return None
    fields = cast(Mapping[str, object], value)
    kind = fields.get("kind")
    reason = _text(fields.get("reason"))
    if kind == "manual" and reason:
        return {"kind": "manual", "reason": reason}
    target_kind = _text(fields.get("targetKind"))
    target_id = _text(fields.get("targetId"))
    correlation_id = _text(fields.get("correlationId"))
    intended = fields.get("intendedConnectionId")
    if (
        kind == "connection"
        and target_kind
        and target_id
        and correlation_id
        and (intended is None or _text(intended))
    ):
        return {
            "kind": "connection",
            "targetKind": target_kind,
            "targetId": target_id,
            "intendedConnectionId": _text(intended),
            "correlationId": correlation_id,
        }
    return None


def _human_handoff(result: Mapping[str, object]) -> Handoff | None:
    handoff = result.get("humanHandoff")
    if not isinstance(handoff, Mapping):
        return None
    fields = cast(Mapping[str, object], handoff)
    url = _text(fields.get("url"))
    expires_at = _text(fields.get("expiresAt"))
    action = _text(fields.get("action"))
    account = fields.get("account")
    resume = _resume(fields.get("resume"))
    if (
        fields.get("kind") != "human_action_required"
        or not url
        or not expires_at
        or not action
        or not isinstance(account, Mapping)
        or not resume
    ):
        return None
    account_fields = cast(Mapping[str, object], account)
    account_id = account_fields.get("id")
    account_name = account_fields.get("name")
    if (
        not isinstance(account_id, int)
        or isinstance(account_id, bool)
        or account_id <= 0
        or not isinstance(account_name, str)
    ):
        return None
    return Handoff(
        kind="human_action_required",
        url=url,
        account={"id": str(account_id), "name": account_name},
        action=action,
        expires_at=expires_at,
        resume=resume,
    )


def _approval(result: Mapping[str, object]) -> Handoff | None:
    approval = result.get("approval")
    if result.get("action") != "approval_required" or not isinstance(approval, Mapping):
        return None
    fields = cast(Mapping[str, object], approval)
    approval_id = _text(fields.get("id"))
    kind = _text(fields.get("kind"))
    state = fields.get("state")
    url = _text(fields.get("url"))
    expires_at = _text(fields.get("expiresAt"))
    account_id = _text(fields.get("targetCustomerId"))
    if (
        not approval_id
        or not kind
        or state not in get_args(ApprovalState)
        or not url
        or not expires_at
        or not account_id
    ):
        return None
    return Handoff(
        kind="approval_required",
        url=url,
        account={"id": account_id, "name": None},
        action=kind,
        expires_at=expires_at,
        resume={
            "kind": "approval",
            "approvalId": approval_id,
            "state": cast(ApprovalState, state),
        },
    )


def find_handoff(result: Mapping[str, object] | None) -> Handoff | None:
    """Recognise a human handoff or a web approval in any operation's result.

    Returns None when the result asks nothing of a person.
    """
    if result is None:
        return None
    return _human_handoff(result) or _approval(result)
