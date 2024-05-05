import pytest

from src.settings.service import ToggleSettingService


@pytest.mark.asyncio(scope='session')
async def test_toggling_with_setting(get_session):
    session = get_session
    serv = ToggleSettingService(session)

    res = await serv.toggle_setting(1, 'weather')

    assert res


@pytest.mark.asyncio(scope='session')
async def test_toggling_without_setting(get_session):
    session = get_session
    serv = ToggleSettingService(session)

    res = await serv.toggle_setting(1, 'news')

    assert res
