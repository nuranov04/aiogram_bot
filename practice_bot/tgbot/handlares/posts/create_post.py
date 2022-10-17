from aiogram import types
from aiogram.dispatcher import FSMContext

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
    await PostState.photo.set()
    await message.answer(text='send me photo')


@dp.message_handler(content_types=[types.ContentType.DOCUMENT], state=PostState.photo)
async def get_post_image(message: types.Message, state: FSMContext):
    await dp.bot.download_file_by_id(message.document.thumb.file_id,
                                     destination=f'../images/{message.document.file_name}')
    async with state.proxy() as data:
        file = await message.document.get_file()
        # print(await )
        with open(f"../images/{message.document.file_name}", 'rb') as f:
            data['photo'] = f
            data['user'] = message.from_user.id
            print(message.from_user.id)
            print(dict(data.items()))
            async with aiohttp.ClientSession() as session:
                async with session.post(url=f"{API}posts/", data=dict(data.items())) as resp:
                    print(resp.status)
                    c = await resp.text()
                    print(c)
