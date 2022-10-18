from aiogram import types

from tgbot.filters.commands import CommandMenu
from tgbot.keyboards.inline.start_keyboard import get_main_menu

from loader import dp


@dp.message_handler(CommandMenu())
async def tg_menu(message: types.Message):
    await message.answer(text=message.from_user.first_name, reply_markup=get_main_menu())
