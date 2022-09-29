import asyncio

from aiogram import Bot, Dispatcher, executor

from conf import Conf


loop = asyncio.get_event_loop()
bot = Bot(token=Conf.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot, loop=loop)


if __name__ == "__main__":
    from handlers import dp, send_message_to_admin
    executor.start_polling(dp, on_startup=send_message_to_admin)

