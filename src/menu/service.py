from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
import aiohttp
from typing import Optional

from src.models import User
from src.config import Settings


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


class GetJokeService:

    def __init__(self, session: aiohttp.ClientSession,
                 settings: Settings) -> None:
        self._session = session
        self._settings = settings

    async def get_joke(self) -> Optional[str]:
        url = self._settings.JOKE_API_URL
        async with self._session.get(url) as resp:
            response = await resp.json()
        if not response['response']:
            answer = f"{response['joke']}"
            return answer
        else:
            return 'Случилась непредвиденная ошибка'
