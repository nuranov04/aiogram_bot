from aiogram import types

from tgbot.filters.get_my_id import CommandGetMyId
from loader import dp


@dp.message_handler(CommandGetMyId())
async def tg_get_my_id(message: types.Message):
    await message.answer(text=f"<b>your id:</b> {message.from_user.id}", parse_mode='HTML')
