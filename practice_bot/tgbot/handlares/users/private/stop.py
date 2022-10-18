from aiogram import types

from tgbot.filters.stop import CommandStop

from loader import dp


@dp.message_handler(CommandStop())
async def tg_stop(message: types.Message):
    await message.answer(text=message.text)
