import pytest_asyncio
from sqlalchemy import insert

from src.db import engine, async_session
from src.models import BaseModel, PreparedMessages


@pytest_asyncio.fixture(scope='session', autouse=True)
async def get_session():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)
    async with async_session() as s:
        message_query = (
                insert(PreparedMessages)
                .values([{'message_id': 'dummy',
                          'message_text': 'fake'}])
            )
        await s.execute(message_query)
        yield s
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
