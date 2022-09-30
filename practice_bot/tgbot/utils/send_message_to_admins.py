import logging

from aiogram import Dispatcher, types

from tgbot.data import config


async def send_notify_startup(dp: Dispatcher):
    try:
        await dp.bot.send_message(chat_id=config.ADMIN_IDS, text='<pre>Bot is ready</>', parse_mode='HTML')
    except Exception as error:
        logging.exception(error)


async def set_default_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands(
        [
            types.BotCommand("start", 'For starting bot'),
            types.BotCommand("help", 'For helping'),
            types.BotCommand("stop", 'For stop'),
        ]
    )
