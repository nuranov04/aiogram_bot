from aiogram import types
from aiogram.dispatcher import FSMContext

import aiohttp

from tgbot.data.config import API
from loader import dp
from tgbot.utils.states import PostState


@dp.callback_query_handler(text='posts')
async def show_my_posts(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API}users/{message.from_user.id}/") as resp:
            user = await resp.json()
            print(user)
            print(user.posts)
