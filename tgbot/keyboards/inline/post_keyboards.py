from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_keyboard(*, last_page, next_page=None, prev_page=None, ):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="First", callback_data=f'first:0'),
            InlineKeyboardButton(text="Previous", callback_data=f'page:{prev_page}'),
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}'),
            InlineKeyboardButton(text="Last", callback_data=f"last:{last_page}")
        ],
        [
            InlineKeyboardButton(text='Back', callback_data='exit pagination')
        ],
    ])
    return keyboard


def get_prev_keyboard(*, prev_page):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="First", callback_data=f'first:0'),
            InlineKeyboardButton(text="Prev", callback_data=f'page:{prev_page}'),

        ],
        [
            InlineKeyboardButton(text='Back', callback_data='exit pagination')
        ]
    ])
    return keyboard


def get_next_keyboard(*, next_page, last_page):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}'),
            InlineKeyboardButton(text="Last", callback_data=f"last:{last_page}")
        ],
        [
            InlineKeyboardButton(text='Back', callback_data='exit pagination')
        ]
    ])
    return keyboard


def get_pagination_keyboard(*, data, page):
    keyboard = None
    if page == 0:
        keyboard = get_next_keyboard(next_page=page + 1, last_page=len(data['data']))
    elif len(data['data']) - 1 == page:
        keyboard = get_prev_keyboard(prev_page=page - 1)
    elif page != 0 and len(data['data']) > page:
        keyboard = get_keyboard(last_page=len(data['data']), next_page=page + 1, prev_page=page - 1)
    return keyboard
