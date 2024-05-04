import pytest

from src.service import GetStartMessageService


@pytest.mark.asyncio(scope='session')
async def test_succesful_get_message(get_session):
    session = get_session
    serv = GetStartMessageService(session)

    res = await serv.get_start_message('dummy')

    assert res == 'fake'
