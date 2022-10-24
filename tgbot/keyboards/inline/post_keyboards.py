from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_keyboard(*, post_id, next_page=None, prev_page=None) -> InlineKeyboardMarkup:
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


def get_pagination_keyboard(*, post_count: int, page: int or str, post_id: int or str) -> InlineKeyboardMarkup:
    """

    :param post_count: Count of user's posts
    :param page: Current page
    :param post_id: post id
    :return: InlineKeyboardMarkup
    """
    keyboard = None
    if page == 0:
        keyboard = get_next_keyboard(next_page=page + 1, post_id=post_id)
    elif post_count == page:
        keyboard = get_prev_keyboard(prev_page=page - 1, post_id=post_id)
    elif page != 0 and post_count > page:
        keyboard = get_keyboard(prev_page=page, post_id=post_id)
    return keyboard


def get_back_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Exit', callback_data='exit pagination')
        ]])
    return keyboard
