from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.fsm import Navigation
from src.db import async_session
from src.service import GetStartMessageService


router = Router()


@router.message(CommandStart())
async def handle_start_command(message: Message, state: FSMContext) -> None:
    async with async_session() as s:
        service = GetStartMessageService(s)
        response = await service.get_start_message('start')
    if response:
        await message.answer(response, reply_markup=)
        await state.set_state(Navigation.menu)

@router.message()
