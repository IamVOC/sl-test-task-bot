from aiogram.utils.keyboard import ReplyKeyboardBuilder
from functools import lru_cache


@lru_cache
def get_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.adjust(2, 2)
    builder.button(text='Погода')
    builder.button(text='Новость')
    builder.button(text='Шутка')
    builder.button(text='Настройки')

    return builder.as_markup()
