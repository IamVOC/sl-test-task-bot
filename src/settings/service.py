from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update
from typing import Optional

from src.models import UserSetting


class ToggleSettingService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def toggle_setting(self, chat_id: int,
                             setting_type: str) -> Optional[bool]:
        existance_query = (
                    select(UserSetting.setting_allowed)
                    .where(UserSetting.chat_id == chat_id)
                    .where(UserSetting.setting_type == setting_type)
                )
        blocked = await self._session.scalar(existance_query)
        if blocked is not None:
            update_query = (
                        update(UserSetting)
                        .where(UserSetting.chat_id == chat_id)
                        .where(UserSetting.setting_type == setting_type)
                        .values(setting_allowed=not blocked)
                    )
            await self._session.execute(update_query)
            await self._session.commit()
            return not blocked
        else:
            insert_query = (
                        insert(UserSetting)
                        .values({'chat_id': chat_id,
                                 'setting_type': setting_type,
                                 'setting_allowed': True})
                    )
            await self._session.execute(insert_query)
            await self._session.commit()
            return True
