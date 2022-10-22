from aiogram import types
from aiogram.dispatcher import FSMContext

import aiohttp

from tgbot.data.config import API
from loader import dp
from tgbot.keyboards.inline.start_keyboard import get_main_menu
from tgbot.utils.states import PostState


@dp.callback_query_handler(text='publish')
async def get_post(callback: types.CallbackQuery):
    await PostState.title.set()
    await callback.message.answer(text='Hi, send me title!')


@dp.message_handler(state=PostState.title)
async def get_post_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await PostState.description.set()
    await message.answer(text='send me description')


@dp.message_handler(state=PostState.description)
async def get_post_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await PostState.image_url.set()
    await message.answer(text='send me photo\'s link')


@dp.message_handler(state=PostState.image_url, regexp='https://*')
async def get_post_image(message: types.Message, state: FSMContext):
    if message.text.startswith('https://'):
        async with state.proxy() as data:
            data['user'] = message.from_user.id
            data['image'] = message.text
            post_data = {
                "title": data["title"],
                "description": data["description"],
                'user': data['user'],
                "image": data['image']
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(url=f"{API}posts/", data=post_data) as resp:
                    c = await resp.json()
                    image_url = c['image']
                    # with open(f'./images/{image_url.split("/")[-1]}', 'wb') as file:
                    #     async with session.get(image_url) as resp2:
                    #         file.write(await resp2.read())
                    if resp.status == 201:
                        await message.answer_photo(photo=c['image'],
                                                   caption="<b>{title}</b>\n\n{desc}\n".format(
                                                       title=c['title'],
                                                       desc=c['description']), parse_mode='HTML')
                        await message.answer(text='you created post!', reply_markup=get_main_menu())
            await state.finish()
    else:
        await message.answer(text='send my only link')
