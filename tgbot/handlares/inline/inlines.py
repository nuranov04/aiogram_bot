import hashlib

from aiogram import types

from loader import dp


@dp.inline_handler()
async def inline_get_my_id(inline_query: types.InlineQuery):
    text = inline_query.query or 'echo'
    link = "https://ru.wikipedia.org/wiki/"+text
    input_content = types.InputTextMessageContent(message_text=link)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = [types.InlineQueryResultArticle(
        id=result_id,
        title=f'Статья википедия',
        input_message_content=input_content,
        url=link
    )]
    await inline_query.answer(item, cache_time=1, is_personal=True)
