from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_keyboard(*, last_page, post_id, next_page=None, prev_page=None):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="First", callback_data=f'first:0'),
            InlineKeyboardButton(text="Previous", callback_data=f'page:{prev_page}'),
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}'),
            InlineKeyboardButton(text="Last", callback_data=f"last:{last_page}")
        ],
        [
            InlineKeyboardButton(text='Back', callback_data='exit pagination'),
            InlineKeyboardButton(text='delete', callback_data=f'delete:{post_id}'),
        ],
    ])
    return keyboard


def get_prev_keyboard(*, prev_page, post_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="First", callback_data=f'first:0'),
            InlineKeyboardButton(text="Prev", callback_data=f'page:{prev_page}'),

        ],
        [
            InlineKeyboardButton(text='Back', callback_data='exit pagination'),
            InlineKeyboardButton(text='Delete', callback_data=f'delete:{post_id}')
        ]
    ])
    return keyboard


def get_next_keyboard(*, next_page, last_page, post_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}'),
            InlineKeyboardButton(text="Last", callback_data=f"last:{last_page}")
        ],
        [
            InlineKeyboardButton(text='Back', callback_data='exit pagination'),
            InlineKeyboardButton(text='Delete', callback_data='delete:{post_id}'),
        ]
    ])
    return keyboard


def get_pagination_keyboard(*, data, page, post_id):
    keyboard = None
    if page == 0:
        keyboard = get_next_keyboard(next_page=page + 1, last_page=len(data['data']), post_id=post_id)
    elif len(data['data']) - 1 == page:
        keyboard = get_prev_keyboard(prev_page=page - 1, post_id=post_id)
    elif page != 0 and len(data['data']) > page:
        keyboard = get_keyboard(last_page=len(data['data']), next_page=page + 1, prev_page=page - 1, post_id=post_id)
    return keyboard
