from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from tgbot.keyboards.inline.post_keyboards import (
    get_pagination_keyboard,
    get_next_keyboard,
    get_back_keyboard
)
from tgbot.utils.get_post import (
    get_user_posts,
    get_user_post
)
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(text='posts')
async def show_my_posts(call: types.CallbackQuery, state: FSMContext):
    posts = await get_user_posts(user_id=call.from_user.id)
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
        page = int(call.data.split(":")[1])
        post_id = data['data'][page]
        post = await get_user_post(post_id=post_id)
        image_url = post['image']
        await call.message.answer_photo(photo=image_url,
                                        caption="<b>{title}</b>\n\n{desc}\n".format(title=post['title'],
                                                                                    desc=post['description']),
                                        reply_markup=get_pagination_keyboard(post_count=len(data['data']), page=page,
                                                                             post_id=post['id'], data=data['data']))
        await call.message.delete()
