from aiogram.utils.keyboard import ReplyKeyboardBuilder
from functools import lru_cache


@lru_cache
def get_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Погода')
    builder.button(text='Новость')
    builder.button(text='Шутка')
    builder.button(text='Настройки')
    builder.adjust(2, 2)

    return builder.as_markup()


@lru_cache
def get_settings_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Переключить доступ к погоде')
    builder.button(text='Переключить доступ к новостям')
    builder.button(text='Выйти в меню')
    builder.adjust(2, 1)

    return builder.as_markup()


@lru_cache
def get_weather_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Омск')
    builder.button(text='Дубай')
    builder.button(text='Выйти')
    builder.adjust(2, 1)

    return builder.as_markup()


@lru_cache
def get_news_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text='tesla')
    builder.button(text='apple')
    builder.button(text='Выйти')
    builder.adjust(2, 1)

    return builder.as_markup()
