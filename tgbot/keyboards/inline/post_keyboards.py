from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_main_post_keyboard(*, post_id, next_page, prev_page) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Previous", callback_data=f'page:{prev_page}'),
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}'),
        ],
        [
            InlineKeyboardButton(text='Exit', callback_data='exit pagination'),
            InlineKeyboardButton(text='delete', callback_data=f'delete:{post_id}'),
        ],
    ])
    return keyboard


def get_prev_keyboard(*, prev_page, post_id) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Prev", callback_data=f'page:{prev_page}'),

        ],
        [
            InlineKeyboardButton(text='Exit', callback_data='exit pagination'),
            InlineKeyboardButton(text='Delete', callback_data=f'delete:{post_id}')
        ]
    ])
    return keyboard


def get_next_keyboard(*, next_page: int or str, post_id: int or str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}'),
        ],
        [
            InlineKeyboardButton(text='Exit', callback_data='exit pagination'),
            InlineKeyboardButton(text='Delete', callback_data=f'delete:{post_id}'),
        ]
    ])
    return keyboard


def get_pagination_keyboard(*, post_count: int or str, page: int or str, post_id: int or str,
                            data: list[int, str]) -> InlineKeyboardMarkup:
    """
    :param post_count: Count of user's posts
    :param page: Current page
    :param post_id: post id
    :param data: list of posts id
    :return: InlineKeyboardMarkup
    """
    keyboard = None
    page = int(page)
    post_count = int(post_count) - 1
    if page == 0:
        keyboard = get_next_keyboard(next_page=page + 1, post_id=data[page + 1])
    elif page == post_count:
        keyboard = get_prev_keyboard(prev_page=page - 1, post_id=data[page - 1])
    elif post_count > page:
        keyboard = get_main_post_keyboard(post_id=post_id, next_page=page+1, prev_page=page-1)
    return keyboard


def get_back_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Exit', callback_data='exit pagination')
        ]])
    return keyboard
