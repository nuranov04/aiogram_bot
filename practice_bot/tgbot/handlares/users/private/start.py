from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

import aiohttp

from tgbot.data.config import API
from loader import dp
from tgbot.keyboards.inline import start_keyboard


@dp.message_handler(CommandStart())
async def tg_start(message: types.Message):
    await message.answer(
        f"Hi, {message.from_user.first_name if message.from_user.first_name else message.from_user.username}",
        reply_markup=start_keyboard.get_main_menu()
    )
    async with aiohttp.ClientSession() as session:
        data_user = {
            "id_telegram": message.from_user.id,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
            "username_telegram": message.from_user.username,
            'password': message.from_user.username
        }
        await session.post(url=f"{API}users/", data=data_user)
