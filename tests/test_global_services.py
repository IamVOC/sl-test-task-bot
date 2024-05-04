import pytest

from src.service import GetStartMessageService, GetSettingService


@pytest.mark.asyncio(scope='session')
async def test_succesful_get_message(get_session):
    session = get_session
    serv = GetStartMessageService(session)

    res = await serv.get_start_message('dummy')

    assert res == 'fake'


@pytest.mark.asyncio(scope='session')
async def test_succesful_get_setting(get_session):
    session = get_session
    serv = GetSettingService(session)

    res = await serv.get_setting_message(1, 'weather')

    assert not res
