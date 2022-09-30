from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def tg_start(message: types.Message):
    await message.answer(
        f"Hi, {message.from_user.first_name if message.from_user.first_name else message.from_user.username}")
