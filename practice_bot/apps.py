from aiogram import executor

from tgbot.utils.send_message_to_admins import send_notify_startup, set_default_commands
from loader import dp


async def run(dispatcher):

    await set_default_commands(dispatcher)

    await send_notify_startup(dispatcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=run)
