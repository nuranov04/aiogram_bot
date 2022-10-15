from aiogram.dispatcher.filters.state import StatesGroup, State


class PostState(StatesGroup):
    title = State()
    description = State()
    photo = State()

