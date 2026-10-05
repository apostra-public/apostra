import asyncio
import os

from apostra import AsyncApostra, paginate_async
from apostra.models import GetDeliveryInput, GetDeliveryResult

async def main() -> None:
    # One deadline includes readiness, discovery and every reporting page.
    async with asyncio.timeout(30), AsyncApostra(
        api_key=os.environ['APOSTRA_API_KEY'],
        account_id=os.environ['APOSTRA_ACCOUNT_ID'],
        base_url=os.environ.get('APOSTRA_BASE_URL', 'https://api.interchange.io/api/v3'),
    ) as api:
        status = await api.get_status({})
        sources = await api.search({'kind': 'inventory_source', 'limit': 20})
        assert status['account'] and sources.get('objects')
        query: GetDeliveryInput = {
            'report': 'campaign_delivery',
            'filters': {'campaignId': os.environ['APOSTRA_CAMPAIGN_ID']},
            'range': {'startDate': os.environ['APOSTRA_START_DATE'], 'endDate': os.environ['APOSTRA_END_DATE']},
            'limit': 100,
        }
        async def read_page(cursor: str | None) -> GetDeliveryResult:
            page_input = query.copy()
            if cursor:
                page_input['cursor'] = cursor
            return await api.get_delivery(page_input)

        pages = 0
        async for page in paginate_async(
            read_page,
            lambda page: page['page'].get('nextCursor') if page['report'] != 'live_campaign_delivery' else None,
        ):
            pages += 1
            if page['report'] == 'live_campaign_delivery':
                continue
        assert pages > 0
        # Keep the complete-window read above, but require the threshold on the
        # one UTC day that provisioning simulated.
        simulated_day_query: GetDeliveryInput = {
            **query,
            'range': {
                'startDate': os.environ['DELIVERY_DATE'],
                'endDate': os.environ['DELIVERY_DATE'],
            },
        }
        async def read_simulated_day_page(cursor: str | None) -> GetDeliveryResult:
            page_input = simulated_day_query.copy()
            if cursor:
                page_input['cursor'] = cursor
            return await api.get_delivery(page_input)

        simulated_day_pages = 0
        observed_impressions = 0.0
        async for page in paginate_async(
            read_simulated_day_page,
            lambda page: page['page'].get('nextCursor') if page['report'] != 'live_campaign_delivery' else None,
        ):
            simulated_day_pages += 1
            if page['report'] == 'live_campaign_delivery':
                continue
            totals = page.get('totals')
            if totals is None:
                continue
            impression_metric = totals['metrics'].get('impressions')
            if impression_metric is None:
                continue
            impressions = impression_metric['value']
            if isinstance(impressions, (int, float)) and not isinstance(impressions, bool):
                observed_impressions = max(observed_impressions, float(impressions))
        assert simulated_day_pages > 0
        minimum_impressions = float(os.environ.get('APOSTRA_MIN_IMPRESSIONS', '0'))
        if minimum_impressions < 0:
            raise ValueError('APOSTRA_MIN_IMPRESSIONS must be a non-negative number')
        if observed_impressions < minimum_impressions:
            raise AssertionError(
                f'Delivery impressions {observed_impressions} are below {minimum_impressions}'
            )

if __name__ == '__main__':
    asyncio.run(main())
