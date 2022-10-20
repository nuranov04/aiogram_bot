from aiogram import types

import aiohttp

from tgbot.data.config import API
from loader import dp
from tgbot.keyboards.inline.post_keyboards import get_keyboard
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(text='posts')
async def show_my_posts(call: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API}users/{call.from_user.id}/") as resp:
            user = await resp.json()
            posts = user['post']
            if len(posts) == 0:
                await call.message.answer(text='you don\'t have any posts')
            else:
                first_post = posts[0]
                if len(posts) == 1:
                    await dp.bot.send_photo(
                        chat_id=call.from_user.id,
                        photo=first_post['image'],
                        caption="<b>{title}</b>\n\n{desc}\n".format(
                            title=first_post['title'],
                            desc=first_post['description']))
                else:
                    await dp.bot.send_photo(
                        chat_id=call.from_user.id,
                        photo=first_post['image'],
                        caption="<b>{title}</b>\n\n{desc}\n".format(
                            title=first_post['title'],
                            desc=first_post['description']), reply_markup=get_keyboard())
                    PaginationState.page.set()

@dp.callback_query_handler(state=PaginationState.page)
async def
