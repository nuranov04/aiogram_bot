import aiohttp

from tgbot.data.config import API


async def get_user_posts(*, user_id: int or str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=f"{API}users/{user_id}/") as resp:
                user_data = await resp.json()
                return user_data['post']
    except KeyError:
        return []

async def get_user_post(*, post_id: int or str, ):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API}posts/{post_id}") as resp:
            return await resp.json()


async def delete_user_post(*, post_id: int or str):
    async with aiohttp.ClientSession() as session:
        async with session.delete(url=f"{API}posts/{post_id}") as resp:
            return await resp.text()


async def like_post(*, user_id, post_id):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=f"{API}likes/", data={"post": post_id, "user": user_id}) as resp:
            return resp.status


async def create_post(*, post_data):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=f"{API}posts/", data=post_data) as resp:
                print(resp.status)
                print(await resp.json())
                return resp.status
    except Exception:
        raise Exception("Error in create post")