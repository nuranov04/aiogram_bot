from aiogram import types
from aiogram.dispatcher import FSMContext

import aiohttp

from tgbot.data.config import API
from loader import dp
from tgbot.keyboards.inline.post_keyboards import (
    get_pagination_keyboard,
    get_next_keyboard,
    get_back_keyboard
)
from tgbot.keyboards.inline.start_keyboard import get_main_menu
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(text='posts')
async def show_my_posts(call: types.CallbackQuery, state: FSMContext):
    start = datetime.datetime.now()
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API}users/{call.from_user.id}/") as resp:
            user = await resp.json()
            posts = user['post']
            await call.message.delete()
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
                            desc=first_post['description']),
                        reply_markup=get_back_keyboard())

                else:
                    await PaginationState.page.set()
                    await dp.bot.send_photo(
                        chat_id=call.from_user.id,
                        photo=first_post['image'],
                        caption="<b>{title}</b>\n\n{desc}\n".format(
                            title=first_post['title'],
                            desc=first_post['description']),
                        reply_markup=get_next_keyboard(next_page=1, last_page=len(posts), post_id=first_post['id']))
                    async with state.proxy() as data:
                        data['data'] = posts
    finish = datetime.datetime.now()
    print(finish - start)


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == 'page', state=PaginationState.page)
async def get_pagination_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.answer()
        page = int(call.data.split(":")[1])

        post = data['data'][page]

        image_url = post['image']

        await call.message.answer_photo(photo=image_url,
                                        caption="<b>{title}</b>\n\n{desc}\n".format(title=post['title'],
                                                                                    desc=post['description']),
                                        reply_markup=get_pagination_keyboard(data=data, page=page, post_id=post['id']))
        await call.message.delete()


@dp.callback_query_handler(lambda call: call.data.split()[0] == 'exit')
async def exit_pagination(call: types.CallbackQuery):
    print(call.data)
    await call.message.answer(text=call.from_user.username, reply_markup=get_main_menu())
    print('some`')
    await call.message.delete()


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == 'last', state=PaginationState.page)
async def show_last_page(call: types.CallbackQuery, state: FSMContext):
    page = int(call.data.split(":")[-1])
    async with state.proxy() as data:
        post = data['data'][page - 1]
    await call.message.answer_photo(photo=post['image'],
                                    caption="<b>{title}</b>\n\n{desc}\n".format(title=post['title'],
                                                                                desc=post['description']),
                                    reply_markup=get_pagination_keyboard(data=data, page=page - 1, post_id=post['id']))
    await call.message.delete()


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == 'first', state=PaginationState.page)
async def show_first_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        post = data['data'][0]
    await call.message.answer_photo(photo=post['image'],
                                    caption="<b>{title}</b>\n\n{desc}\n".format(title=post['title'],
                                                                                desc=post['description']),
                                    reply_markup=get_pagination_keyboard(data=data, page=0, post_id=post['id']))

    await call.message.delete()


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == "delete", state=PaginationState.page)
async def delete_post(call: types.CallbackQuery):
    url = f"{API}posts/{call.data.split(':')[1]}"

    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as resp:
            print(resp.status)
            if resp.status == 204:
                await call.message.answer(text=call.from_user.username, reply_markup=get_main_menu())
                await call.message.delete()
