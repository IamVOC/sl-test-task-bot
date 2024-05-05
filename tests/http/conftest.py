import pytest_asyncio
import aiohttp


@pytest_asyncio.fixture
async def get_client():
    async with aiohttp.ClientSession() as s:
        yield s
