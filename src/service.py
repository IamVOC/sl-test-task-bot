from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from src.models import PreparedMessage
from src.models import UserSetting


class GetStartMessageService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_start_message(self, message_id: str) -> Optional[str]:
        stmt = (
                select(PreparedMessage.message_text)
                .where(PreparedMessage.message_id == message_id)
            )

        res = await self._session.scalar(stmt)
        return res


class GetSettingService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_setting_message(self, chat_id: int,
                                  setting_type: str) -> Optional[bool]:
        stmt = (
                select(UserSetting.setting_allowed)
                .where(UserSetting.chat_id == chat_id)
                .where(UserSetting.setting_type == setting_type)
            )

        res = await self._session.scalar(stmt)
        return res
