from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.data import config

bot = Bot(token=config.TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

