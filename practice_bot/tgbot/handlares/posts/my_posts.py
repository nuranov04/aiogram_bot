from aiogram import types
from aiogram.dispatcher import FSMContext

import aiohttp
import logging
import os

from tgbot.data.config import API
from loader import dp
from tgbot.keyboards.inline.post_keyboards import get_keyboard, get_next_keyboard, get_prev_keyboard
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(text='posts')
async def show_my_posts(call: types.CallbackQuery, state: FSMContext):
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
                    async with state.proxy() as data:
                        data['data'] = posts


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == 'page', state=PaginationState.page)
async def get_pagination_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.answer()
        print(data)
        page = int(call.data.split(":")[1])

        post = data['data'][page]

        image_url = post['image']

        if len(data['data'])-1 == page:
            keyboard = get_prev_keyboard(prev_page=page - 1)
        elif page != 0 and len(data['data']) > page:
            keyboard = get_keyboard(next_page=page + 1, prev_page=page - 1)
        elif page == 0:
            keyboard = get_next_keyboard(next_page=page + 1)

        await call.message.delete()
        await call.message.answer_photo(photo=image_url,
                                        caption="<b>{title}</b>\n\n{desc}\n".format(title=post['title'],
                                                                                    desc=post[
                                                                                        'description']),
                                        reply_markup=keyboard)

        # print(filename)
        # print(os.path.exists(f"../images/{filename}"))
        # if os.path.exists(f"../images/{filename}"):
        #     await call.message.edit_media(media=types.InputMedia(open(f"../images/{filename}")))
        # else:
        #     with open(f'../images/{filename}', 'wb') as file:
        #         async with session.get(image_url) as resp2:
        #             file.write(await resp2.read())
        #     await call.message.edit_media(media=types.InputMedia(open(f"../images/{filename}")))
