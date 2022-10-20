from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Next", callback_data='next'),
            InlineKeyboardButton(text="Previous", callback_data='prev')
        ],
    ])
    return keyboard
