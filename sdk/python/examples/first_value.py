import os
from uuid import uuid4

from apostra import Apostra


def required(name: str) -> str:
    value = os.environ.get(name)
    if value is None or value == '':
        raise RuntimeError(f'{name} is required')
    return value


with Apostra(
    api_key=required('APOSTRA_API_KEY'),
    account_id=os.environ.get('APOSTRA_ACCOUNT_ID'),
    base_url=os.environ.get('APOSTRA_BASE_URL', 'https://api.apostra.com/api/v3'),
) as api:
    campaign_id = required('APOSTRA_CAMPAIGN_ID')

    # Verify the credential and discover the resolved account before any write.
    status = api.get_status({})
    if not status.get('account'):
        raise RuntimeError('The credential did not resolve an account')

    # A unique key belongs to this exact preview request. Reuse it only to retry
    # the same request after an uncertain response.
    preview_key = str(uuid4())
    preview = api.save_campaign(
        {
            'campaignId': campaign_id,
            'desiredPhase': 'active',
            'idempotencyKey': preview_key,
        },
        idempotency_key=preview_key,
    )

    # Inspect `preview` before confirming. Confirmation is deliberately opt-in
    # so running the sample against the synthetic seller remains a preview by default.
    if os.environ.get('APOSTRA_CONFIRM_LAUNCH') == 'true':
        confirm_key = str(uuid4())
        api.save_campaign(
            {
                'campaignId': campaign_id,
                'desiredPhase': 'active',
                'confirmLaunch': True,
                'idempotencyKey': confirm_key,
            },
            idempotency_key=confirm_key,
        )

    delivery = api.get_delivery(
        {
            'report': 'campaign_delivery',
            'filters': {'campaignId': campaign_id},
            'range': {
                'startDate': required('APOSTRA_START_DATE'),
                'endDate': required('APOSTRA_END_DATE'),
            },
            'limit': 100,
        }
    )

    _ = preview, delivery
