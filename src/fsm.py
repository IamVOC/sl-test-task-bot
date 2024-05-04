from aiogram.fsm.state import State, StatesGroup


class Navigation(StatesGroup):
    menu = State()
    weather = State()
    news = State()
    settings = State()
