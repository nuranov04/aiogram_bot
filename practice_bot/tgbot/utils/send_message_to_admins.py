from aiogram import types

from loader import bot
from tgbot.data import config


async def send_notify_startup(disputcher):
    print(dir(message))
    await bot.send_message(chat_id=config.ADMIN_IDS, text='<pre>hello world</>', parse_mode='HTML')


