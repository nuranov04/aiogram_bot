from aiogram import types

import aiohttp

from tgbot.data.config import API
from loader import dp


@dp.callback_query_handler(text='posts')
async def show_my_posts(call: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API}users/{call.from_user.id}/") as resp:
            user = await resp.json()
            print(user)
            print("\n\n\n\n\n")
            print(user['post'])
            for post in user['post'][0]:
                await dp.bot.send_photo(
                    chat_id=call.from_user.id,
                    photo=post['image'],
                    caption="<b>{title}</b>\n\n{desc}\n".format(
                                                   title=post['title'],
                                                   desc=post['description']))
