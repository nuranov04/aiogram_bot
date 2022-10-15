import asyncio
import aiohttp

from tgbot.data.config import API


async def login(user_id, first_name, last_name, username):
    async with aiohttp.ClientSession() as session:
        data = {
            "id_telegram": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "username_telegram": username
        }
        async with session.post(url=f"{API}users/", data=data) as resp:
            if resp.status == 201 or resp.status == 400:
                pass
