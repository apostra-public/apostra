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
        async for _page in paginate_async(
            read_page,
            lambda page: page['page'].get('nextCursor') if page['report'] != 'live_campaign_delivery' else None,
        ):
            pages += 1
        assert pages > 0

if __name__ == '__main__':
    asyncio.run(main())
# The fixture owner must additionally assert non-zero recent delivery totals.
