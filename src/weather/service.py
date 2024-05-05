import aiohttp

from src.config import Settings


class GetWeatherService:

    def __init__(self, session: aiohttp.ClientSession,
                 settings: Settings) -> None:
        self._session = session
        self._settings = settings

    async def get_current_weather(self, city: str) -> str:
        url = f'{self._settings.WEATHER_API_URL}?q={city}&lang=ru&key={self._settings.WEATHER_API_KEY}'
        async with self._session.get(url) as resp:
            response = await resp.json()
        if response:
            answer = f"{response['current']['temp_c']} {response['current']['condition']['text']}"
            return answer
        else:
            return 'Такого города нет'
