from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.fsm import Navigation
from src.db import async_session
from src.service import GetStartMessageService
from src.settings.service import ToggleSettingService
from src.keyboard import get_menu_keyboard


router = Router()


@router.message(Navigation.settings, F.text == 'Переключить доступ к погоде')
async def turn_weather_setting(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        service = ToggleSettingService(s)
        message_service = GetStartMessageService(s)
        complete = await service.toggle_setting(message.chat.id, 'weather')
        if complete is not None:
            if complete:
                response = await message_service.get_start_message(
                        'weather_off')
            else:
                response = await message_service.get_start_message(
                        'weather_on')
            if response:
                await message.answer(response)


@router.message(Navigation.settings, F.text == 'Переключить доступ к новостям')
async def turn_news_setting(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        service = ToggleSettingService(s)
        message_service = GetStartMessageService(s)
        complete = await service.toggle_setting(message.chat.id, 'news')
        if complete is not None:
            if complete:
                response = await message_service.get_start_message(
                        'news_off')
            else:
                response = await message_service.get_start_message(
                        'news_on')
            if response:
                await message.answer(response)


@router.message(Navigation.settings, F.text == 'Выйти в меню')
async def return_to_menu(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        message_service = GetStartMessageService(s)
        response = await message_service.get_start_message('back_to_menu')
        if response:
            await message.answer(response,
                                 reply_markup=get_menu_keyboard())
            await state.set_state(Navigation.menu)
