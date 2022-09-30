from aiogram import executor

from tgbot.utils.send_message_to_admins import send_notify_startup
from loader import dp


async def run():
    await send_notify_startup(disputcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=send_notify_startup)
