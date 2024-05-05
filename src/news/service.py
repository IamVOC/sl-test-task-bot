import aiohttp

from src.config import Settings


class GetNewsService:

    def __init__(self, session: aiohttp.ClientSession,
                 settings: Settings) -> None:
        self._session = session
        self._settings = settings

    async def get_current_news(self, source: str) -> str:
        url = f'{self._settings.NEWS_API_URL}?q={source}&pageSize=1&page=1&apiKey={self._settings.NEWS_API_KEY}'
        async with self._session.get(url) as resp:
            response = await resp.json()
        if response['articles']:
            answer = f"{response['articles'][0]['title']}\n{response['articles'][0]['url']}"
            return answer
        else:
            return 'Такого источника нет'
