from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from src.states.base import (
    CreateChatState,
    MessageState
)
from src.handlers.base_handlers import (
    add_message,
    start,
    create_chat,
)
from src.handlers.state import (
    state_title,
    state_message
)


def register_handlers(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(create_chat, F.text == "Создать чат")
    router.message.register(add_message, F.text == "Добавить сообщение")


    router.message.register(state_title, CreateChatState.title)
    router.message.register(state_message, MessageState.text)