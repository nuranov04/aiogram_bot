from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from tgbot.keyboards.inline.start_keyboard import get_main_menu
from tgbot.utils.states import PaginationState


@dp.callback_query_handler(lambda call: call.data.split()[0] == 'exit', state=PaginationState.page)
async def exit_pagination(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(text=call.from_user.username, reply_markup=get_main_menu())
    await call.message.delete()
