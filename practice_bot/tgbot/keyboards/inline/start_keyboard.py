from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from tgbot.data.config import ADMIN_USERNAME


def get_main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Publish post", callback_data='publish'),
            InlineKeyboardButton(text="Show my posts", callback_data='posts')
        ],
        [
            InlineKeyboardButton(text="Show my followers", callback_data="followers"),
            InlineKeyboardButton(text="My subscriptions", callback_data="subscriptions")
        ],
        [
            InlineKeyboardButton(text="Support", url=f"t.me/{ADMIN_USERNAME}"),
        ]

    ])
    return keyboard
