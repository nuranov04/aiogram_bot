from aiogram import Dispatcher, types


async def set_default_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands(
        [
            types.BotCommand("start", 'For starting bot'),
            types.BotCommand("help", 'For helping'),
            types.BotCommand("stop", 'For stop'),
            types.BotCommand("get_my_id", 'get my telegram id'),
            types.BotCommand("menu", 'show menu'),
        ]
    )
