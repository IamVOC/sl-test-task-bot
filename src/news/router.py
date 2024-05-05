from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiohttp import ClientSession

from src.fsm import Navigation
from src.news.service import GetNewsService
from src.service import GetStartMessageService
from src.config import settings
from src.db import async_session
from src.keyboard import get_menu_keyboard


router = Router()


@router.message(Navigation.news, F.text == 'Выйти')
async def leave_news(message: Message, state: FSMContext):
    async with async_session() as s:
        message_service = GetStartMessageService(s)
        response = await message_service.get_start_message('back_to_menu')
        if response:
            await message.answer(response,
                                 reply_markup=get_menu_keyboard())
            await state.set_state(Navigation.menu)


@router.message(Navigation.news, F.text)
async def get_news(message: Message, state: FSMContext):
    async with ClientSession() as s:
        service = GetNewsService(s, settings)
        response = await service.get_current_news(message.text)
    if response:
        await message.answer(response,
                             reply_markup=get_menu_keyboard())
        await state.set_state(Navigation.menu)
