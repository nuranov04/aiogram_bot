import hashlib

from aiogram import types

from loader import dp


@dp.inline_handler()
async def inline_get_my_id(inline_query: types.InlineQuery):
    # print(inline_query, )
    # print(inline_query.query, )
    # text = inline_query.query
    # print(text)
    # await inline_query.answer(inline_query.from_user.id)
    text = inline_query.query or 'echo'
    link = "https://ru.wikipedia.org/wiki/"+text
    input_content = types.InputTextMessageContent(link)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = [types.InlineQueryResultArticle(
        id=result_id,
        title=f'Статья википедия',
        input_message_content=input_content,
        url=link
    )]
    await inline_query.answer(item, cache_time=1, is_personal=True)
    print(text)
    # await inline_query.answer(results)
    # don't forget to set cache_time=1 for testing (default is 300s or 5m)
    await dp.bot.answer_inline_query(inline_query.id, results=[item])
