from aiogram.dispatcher.filters.state import StatesGroup, State


class PostState(StatesGroup):
    title = State()
    description = State()
    image_url = State()


class PaginationState(StatesGroup):
    page = 0
