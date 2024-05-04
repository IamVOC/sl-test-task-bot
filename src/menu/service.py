from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User


class UserService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def register_user(self, chat_id: int) -> None:
        exist = await self._session.scalar(select(User).
                                           where(User.chat_id == chat_id))
        if not exist:
            await self._session.execute(insert(User).
                                        values({'chat_id': chat_id}))
            await self._session.commit()
