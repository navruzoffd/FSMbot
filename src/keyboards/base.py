from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def start_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Create", callback_data="create"),
         InlineKeyboardButton(text="View", callback_data="view")],
    ])
    return keyboard

def filters_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Age", callback_data="state_age")],
        [InlineKeyboardButton(text="Market Cap", callback_data="state_marketcap")],
        [InlineKeyboardButton(text="Ignore social networks", callback_data="state_ingnore_social")],
        [InlineKeyboardButton(text="5M volume change", callback_data="5m_volume_change")],
        [InlineKeyboardButton(text="Tx 1d", callback_data="tx1d")],
        [InlineKeyboardButton(text="Tx 1h", callback_data="tx1h")],
        [InlineKeyboardButton(text="Tx 5m", callback_data="tx5m")],
        [InlineKeyboardButton(text="Submit", callback_data="submit_alert")],
        [InlineKeyboardButton(text="Back", callback_data="start")],
    ])
    return keyboard

def delete_keyboard(oid: str):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Delete", callback_data=f"delete_{oid}")],
    ])
    return keyboard