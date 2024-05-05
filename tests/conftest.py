import pytest_asyncio
from sqlalchemy import insert

from src.db import engine, async_session
from src.models import BaseModel, PreparedMessage, User, UserSetting


@pytest_asyncio.fixture(scope='session')
async def get_session():
    async with async_session() as s:
        yield s


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)
    async with async_session() as s:
        user_query = (
                insert(User)
                .values([{'chat_id': 1}])
            )
        message_query = (
                insert(PreparedMessage)
                .values([{'message_id': 'dummy',
                          'message_text': 'fake'}])
            )
        user_settings_query = (
                insert(UserSetting)
                .values([{'chat_id': 1,
                          'setting_type': 'weather',
                          'setting_allowed': False}])
            )
        await s.execute(user_query)
        await s.execute(message_query)
        await s.execute(user_settings_query)
        await s.commit()
    yield
#    async with engine.begin() as conn:
#        await conn.run_sync(BaseModel.metadata.drop_all)
