from aiogram.types import Message
from config import settings
from aiohttp import ClientSession


async def state_title(message: Message):
    title = message.text
    data = {
        "title": title
    }

    url = settings.DOMAIN + "chats/"
    async with ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status == 200:
                await message.answer(f"{title} успешно создан")
            elif response.status == 400:
                await message.answer(f"Чат уже был создан")
            else:
                await message.answer(f"Ошибка {response.status}")
    
async def state_message(message: Message):
    text = message.text
    data = {
        "text": text
    }

    url = settings.DOMAIN + f"chats/{message.from_user.id}/messages"
    async with ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status == 200:
                await message.answer(f"Сообщение добавлено")
            else:
                await message.answer(f"Ошибка {response.status}")