from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from tgbot.keyboards.inline.start_keyboard import get_main_menu
from tgbot.utils.get_post import delete_user_post
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(lambda call: call.data.split(":")[0] == "delete", state=PaginationState.page)
async def delete_post(call: types.CallbackQuery, state: FSMContext):
    post_id = call.data.split(":")[1]
    await delete_user_post(post_id=post_id)
    await call.message.answer(text=call.from_user.username, reply_markup=get_main_menu())
    await state.finish()
    await call.message.delete()
