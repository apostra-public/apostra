# mypy: disallow-any-expr
"""Consumer examples against adcp 8.0.0b15; no runtime SDK adapter or schema copy."""

import json
import unittest

from adcp.types import (
    CatalogType,
    ContentIdType,
    Duration,
    DurationUnit,
    EventType,
    FeedFormat,
    UpdateFrequency,
)
from apostra.models import (
    GetDeliverySuccessSchema21,
    SaveCampaignRequestEventGoal,
    SaveCatalogInput,
)


def catalog(
    kind: CatalogType,
    feed: FeedFormat,
    cadence: UpdateFrequency,
    content: ContentIdType,
    event: EventType,
) -> SaveCatalogInput:
    return {
        "catalogId": "catalog",
        "advertiserId": "advertiser",
        "idempotencyKey": "request",
        "type": kind.value,
        "feedFormat": feed.value,
        "updateFrequency": cadence.value,
        "contentIdType": content.value,
        "conversionEvents": [event.value],
    }


def goal(event: EventType) -> SaveCampaignRequestEventGoal:
    return {
        "kind": "event",
        "eventSources": [{"eventSourceId": "source", "eventType": event.value}],
    }


def duration(value: Duration) -> GetDeliverySuccessSchema21:
    # Construct the actual wire dictionary. model_dump() erases its static type.
    # V3's safe-integer maximum remains a server constraint, not an AdCP claim.
    return {"interval": value.interval, "unit": value.unit.value}


def upstream_duration(value: GetDeliverySuccessSchema21) -> Duration:
    return Duration(interval=value["interval"], unit=DurationUnit(value["unit"]))


class AdcpInteropTests(unittest.TestCase):
    def test_enum_composition(self) -> None:
        for kind in CatalogType:
            value = catalog(
                kind,
                FeedFormat.custom,
                UpdateFrequency.daily,
                ContentIdType.sku,
                EventType.purchase,
            )
            self.assertEqual(value.get("type"), kind.value)
        for event in EventType:
            self.assertEqual(goal(event)["eventSources"][0]["eventType"], event.value)

    def test_duration_round_trip(self) -> None:
        for unit in DurationUnit:
            value = Duration(interval=1, unit=unit)
            wire = duration(value)
            self.assertEqual(upstream_duration(wire), value)
            expected: GetDeliverySuccessSchema21 = {"interval": 1, "unit": unit.value}
            self.assertEqual(json.dumps(wire), json.dumps(expected))
