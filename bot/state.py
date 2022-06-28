from aiogram.dispatcher.filters.state import StatesGroup, State


class LaunchState(StatesGroup):
    image = State()
