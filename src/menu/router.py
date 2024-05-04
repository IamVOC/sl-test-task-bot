from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.fsm import Navigation
from src.db import async_session
from src.service import GetStartMessageService
from src.keyboard import get_menu_keyboard


router = Router()


@router.message(CommandStart())
async def handle_start_command(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        service = GetStartMessageService(s)
        response = await service.get_start_message('start')
    if response:
        await message.answer(response, reply_markup=get_menu_keyboard())
        await state.set_state(Navigation.menu)


@router.message(Navigation.menu, F.text == 'Погода')
async def handle_weather_input(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        service = GetStartMessageService(s)
        response = await service.get_start_message('weather')
    if response:
        await message.answer(response, reply_markup=get_menu_keyboard())
        await state.set_state(Navigation.weather)


@router.message(Navigation.menu, F.text == 'Новость')
async def handle_news_input(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        service = GetStartMessageService(s)
        response = await service.get_start_message('news')
    if response:
        await message.answer(response, reply_markup=get_menu_keyboard())
        await state.set_state(Navigation.weather)


@router.message(Navigation.menu, F.text == 'Настройки')
async def handle_settings_input(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        service = GetStartMessageService(s)
        response = await service.get_start_message('settings')
    if response:
        await message.answer(response, reply_markup=get_menu_keyboard())
        await state.set_state(Navigation.weather)
