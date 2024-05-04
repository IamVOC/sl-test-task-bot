from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from src.models import PreparedMessages


class GetStartMessageService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_start_message(self, message_id: str) -> Optional[str]:
        stmt = (
                select(PreparedMessages.message_text)
                .where(PreparedMessages.message_id == message_id)
            )

        res = await self._session.scalar(stmt)
        return res
