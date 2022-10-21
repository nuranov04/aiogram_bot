import logging

from aiogram import Dispatcher

from tgbot.data import config


async def send_notify_startup(dp: Dispatcher):
    try:
        await dp.bot.send_message(chat_id=config.ADMIN_IDS, text='<pre>Bot is ready</>', parse_mode='HTML')
    except Exception as error:
        logging.exception(error)



