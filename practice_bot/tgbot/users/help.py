from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def tg_help(message: types.Message):
    await message.answer(text="It's help text")
