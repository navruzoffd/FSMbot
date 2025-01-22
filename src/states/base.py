from aiogram.filters.state import State, StatesGroup


class CreateAlertState(StatesGroup):
    title = State()
    age_range = State()
    marketcap_range = State()
    ignore_social_networks = State()
    m5_volume_change = State()
    tx1d = State()
    tx1h = State()
    tx5m = State()

class MessageState(StatesGroup):
    text = State()