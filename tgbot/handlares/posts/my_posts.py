from aiogram import types
from aiogram.dispatcher import FSMContext

import datetime

from loader import dp
from tgbot.keyboards.inline.post_keyboards import (
    get_pagination_keyboard,
    get_next_keyboard,
    get_back_keyboard
)
from tgbot.keyboards.inline.start_keyboard import get_main_menu
from tgbot.utils.get_post import (
    get_user_posts,
    delete_user_post,
    get_user_post
)
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(text='posts')
async def show_my_posts(call: types.CallbackQuery, state: FSMContext):
    posts = await get_user_posts(user_id=call.from_user.id)
    print(posts)
    await call.message.delete()
    if len(posts) == 0:
        await call.message.answer(text='you don\'t have any posts')
    elif len(posts) == 1:
        await dp.bot.send_photo(
            chat_id=call.from_user.id,
            photo=posts[0]['image'],
            caption="<b>{title}</b>\n\n{desc}\n".format(
                title=posts[0]['title'],
                desc=posts[0]['description']),
            reply_markup=get_back_keyboard())
    else:
        await dp.bot.send_photo(
            chat_id=call.from_user.id,
            photo=posts[0]['image'],
            caption="<b>{title}</b>\n\n{desc}\n".format(
                title=posts[0]['title'],
                desc=posts[0]['description']),
            reply_markup=get_next_keyboard(next_page=1, post_id=posts[0]['id']))
        await PaginationState.page.set()
        async with state.proxy() as data:
            data['data'] = [i['id'] for i in posts]
            print(data['data'])


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == 'page', state=PaginationState.page)
async def get_pagination_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.answer()
        print(call.data)
        page = int(call.data.split(":")[1])

        post_id = data['data'][page]
        post = await get_user_post(post_id=post_id)
        image_url = post['image']

        await call.message.answer_photo(photo=image_url,
                                        caption="<b>{title}</b>\n\n{desc}\n".format(title=post['title'],
                                                                                    desc=post['description']),
                                        reply_markup=get_pagination_keyboard(post_count=len(data), page=page,
                                                                             post_id=post['id']))
        await call.message.delete()


@dp.callback_query_handler(lambda call: call.data.split()[0] == 'exit', state=PaginationState.page)
async def exit_pagination(call: types.CallbackQuery):
    print(call.data)
    await call.message.answer(text=call.from_user.username, reply_markup=get_main_menu())
    await call.message.delete()


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == "delete", state=PaginationState.page)
async def delete_post(call: types.CallbackQuery):
    post_id = call.data.split(":")[1]
    await delete_user_post(post_id=post_id)
    await call.message.answer(text=call.from_user.username, reply_markup=get_main_menu())
    await call.answer()
    await call.message.delete()
