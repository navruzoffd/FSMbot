from aiogram.types import Message
from src.keyboards.base import start_keyboard
from aiogram.fsm.context import FSMContext
from aiohttp import ClientSession
from config import settings
from src.states.base import (
    CreateChatState,
    MessageState
)


async def start(message: Message) -> None:
    await message.answer("Выберите опцию:", reply_markup=start_keyboard())

async def create_chat(message: Message, state: FSMContext):
    await message.answer("Введите название чата:")
    await state.set_state(CreateChatState.title)

async def add_message(message: Message, state: FSMContext):
    await message.answer("Введите сообщение:")
    await state.set_state(MessageState.text)

async def get_messages(message: Message, state: FSMContext):
    url = settings.DOMAIN + f"chats/{message.from_user.id}"
    async with ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = response.json()
                for message in data:
                    pass
                    ##TODO Развернуть бэк, посмотреть структуру ответов
            else:
                await message.answer(f"Ошибка {response.status}")