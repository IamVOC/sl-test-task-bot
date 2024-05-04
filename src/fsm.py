from aiogram.fsm.state import State, StatesGroup


class Navigation(StatesGroup):
    menu = State()
    weather_choose = State()
    news_choose = State()
