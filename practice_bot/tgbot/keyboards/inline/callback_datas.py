from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext

from tgbot.data.config import ACCESS_TOKEN
from loader import dp


@dp.callback_query_handler(text='publish')
async def publish(callback: types.CallbackQuery):
    await callback.message.answer(text='Send me post\'s title')
    await callback.answer()
