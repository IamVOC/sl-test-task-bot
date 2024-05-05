from aiogram import Dispatcher, Bot
import asyncio

from src.config import settings
from src.menu.router import router as menu_router
from src.settings.router import router as settings_router
from src.weather.router import router as weather_router
from src.news.router import router as news_router


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=settings.TOKEN)

    dp.include_router(menu_router)
    dp.include_router(settings_router)
    dp.include_router(weather_router)
    dp.include_router(news_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
