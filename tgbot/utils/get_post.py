import aiohttp

from tgbot.data.config import API


async def get_user_posts(*, user_id: int or str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API}users/{user_id}/") as resp:
            user_data = await resp.json()
            posts = user_data['post']
            return posts


async def get_user_post(*, post_id: int or str, ):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API}posts/{post_id}") as resp:
            return await resp.json()


async def delete_user_post(*, post_id: int or str):
    async with aiohttp.ClientSession() as session:
        async with session.delete(url=f"{API}posts/{post_id}") as resp:
            print(await resp.text())
            return await resp.text()
