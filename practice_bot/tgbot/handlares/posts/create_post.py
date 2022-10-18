from aiogram import types
from aiogram.dispatcher import FSMContext
from PIL import Image

import aiohttp
import base64
import json

from tgbot.data.config import API
from loader import dp
from tgbot.utils.states import PostState


@dp.callback_query_handler(text='publish')
async def get_post_image(callback: types.CallbackQuery):
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


@dp.message_handler(state=PostState.image_url)
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
                    print(resp.status)
                    c = await resp.text()
                    print(type(c))
                    print(c)
                    print(c['image'])
                    if resp.status == 201:
                        await message.answer_photo(photo=data['image'],
                                                   caption="<br>{title}</br>\n\n{desc}\n".format(
                                                       title=data['title'],
                                                       desc=data['description']), parse_mode='HTML')
                        await message.answer(text='you created post!')
