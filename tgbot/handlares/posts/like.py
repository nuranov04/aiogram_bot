from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from tgbot.utils.get_post import like_post
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(lambda call: call.data.split()[0] == "like", state=PaginationState.page)
async def create_post_like(call: types.CallbackQuery, state: FSMContext):
    post_id = call.data.split()[1]
    user_id = call.from_user.id
    result = await like_post(user_id=user_id, post_id=post_id)
    if result == 201:
        await call.answer("post id created")
    else:
        await call.answer("sorry, but before you liked this post :)")
