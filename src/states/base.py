from aiogram.filters.state import State, StatesGroup


class CreateChatState(StatesGroup):
    title = State()

class MessageState(StatesGroup):
    text = State()