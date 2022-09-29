from bot import bot, dp

from aiogram.types import Message
from conf import Conf


async def send_message_to_admin(dp):
    await bot.send_message(chat_id=Conf.ADMIN_ID, text='bot is ready')


@dp.message_handler()
async def echo(message: Message):
    # await bot.send_message(chat_id=message.chat.id, text=text)
    await message.answer(text=message.text)
