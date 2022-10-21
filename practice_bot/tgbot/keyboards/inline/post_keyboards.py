from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_keyboard(next_page=None, prev_page=None):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Previous", callback_data=f'page:{prev_page}'),
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}') if next_page else None,
        ],
    ])
    return keyboard


def get_prev_keyboard(prev_page):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Prev", callback_data=f'page:{prev_page}'),

        ]
    ])
    return keyboard


def get_next_keyboard(next_page):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Next", callback_data=f'page:{next_page}')
        ],
    ])
    return keyboard
