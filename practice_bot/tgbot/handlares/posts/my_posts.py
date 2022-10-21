from aiogram import types
from aiogram.dispatcher import FSMContext

import aiohttp
import os

from tgbot.data.config import API
from loader import dp
from tgbot.keyboards.inline.post_keyboards import get_keyboard, get_next_keyboard, get_prev_keyboard
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(text='posts')
async def show_my_posts(call: types.CallbackQuery):
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
                    await PaginationState.page.set()
                    await dp.bot.send_photo(
                        chat_id=call.from_user.id,
                        photo=first_post['image'],
                        caption="<b>{title}</b>\n\n{desc}\n".format(
                            title=first_post['title'],
                            desc=first_post['description']), reply_markup=get_next_keyboard(next_page=1))


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == 'page', state=PaginationState.page)
async def get_pagination_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=f"{API}users/{call.from_user.id}/") as resp:
                user = await resp.json()
                data['data'] = user['post']
                page = int(call.data.split(":")[1])
                post = data['data'][page]

                await call.message.edit_media(media=types.InputMedia())
                await call.message.edit_caption(caption="<b>{title}</b>\n\n{desc}\n".format(title=post['title'],
                                                                                            desc=post['description']),
                                                reply_markup=get_keyboard(next_page=page + 1,
                                                                          prev_page=page - 1) if len(
                                                    data['data']) > page + 1 else get_prev_keyboard(prev_page=page - 1))
                await call.answer()
