import re
from aiogram.types import Message, CallbackQuery
from src.keyboards.base import delete_keyboard, start_keyboard
from aiogram.fsm.context import FSMContext
from aiohttp import ClientSession
from config import settings
from src.states.base import (
    CreateAlertState
)


async def start(message: Message | CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    if isinstance(message, Message):
        await message.answer("Alert menu:", reply_markup=start_keyboard())
    else:
        await message.message.answer("Alert menu:", reply_markup=start_keyboard())


async def create_alert(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter name:")
    await state.set_state(CreateAlertState.title)


async def set_age(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter range for age in hours. Default: 24-72")
    await state.set_state(CreateAlertState.age_range)


async def set_marketcap(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter range for marketcap in dollars.\nDefault: 50000-100000")
    await state.set_state(CreateAlertState.marketcap_range)


async def set_ignore_social_networks(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Type "yes" or "no"\nDefault: "no"')
    await state.set_state(CreateAlertState.ignore_social_networks)


async def set_5m_volume_change(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter volume cange % in 5 minutes. Example: 10")
    await state.set_state(CreateAlertState.m5_volume_change)


async def set_tx1d(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter min tx count in 1 day. Example: 1500")
    await state.set_state(CreateAlertState.tx1d)


async def set_tx1h(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter min tx count in 1 hour. Example: 1500")
    await state.set_state(CreateAlertState.tx1h)


async def set_tx5m(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter min tx count in 5 min. Example: 150")
    await state.set_state(CreateAlertState.tx5m)


async def submit_alert_request(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("In process...")

    url = settings.DOMAIN + "/alert/"
    data = await state.get_data()
    request_data = {
        "name": data["title"],
        "chat_id": str(callback.from_user.id),
        "filters": {
            "age": data.get("age_range", "86400 259200").split(),
            "market_cap": data.get("marketcap_range", "50000 100000").split(),
            "ignore_social_networks": data.get("ignore_social_networks"),
            "m5_volume_change": data.get("m5_volume_change"),
            "tx1d": data.get("tx1d"),
            "tx1h": data.get("tx1h"),
            "tx5m": data.get("tx5m")
        }
    }
    async with ClientSession() as session:
        async with session.post(url=url, json=request_data) as response:
            response_data = await response.json()
            if response.status == 201:
                await callback.message.answer("Success✅")
            else:
                await callback.message.answer(str(response_data))


async def get_alerts(callback: CallbackQuery):
    await callback.message.answer("In process...")

    url = settings.DOMAIN + "/alert/list/" + str(callback.from_user.id)
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            response_data = await response.json()
            if response.status == 200:
                await callback.message.answer(f"Alerts count: {response_data["count"]}")
                for message in response_data["items"]:
                    answer = f"name: {message["name"]}\n"
                    answer += "filters:\n"
                    for k, v in message["filters"].items():
                        answer += f"\t\t{k}: {v}\n"
                    await callback.message.answer(re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', answer), reply_markup=delete_keyboard(message["oid"]))
                    answer = ""
            else:
                await callback.message.answer(str(response_data))


async def delete_alert(callback: CallbackQuery):
    oid = callback.data.split("_")[1]
    async with ClientSession() as session:
        url = settings.DOMAIN + "/alert/" + oid
        async with session.delete(url=url) as response:
            response_data = await response.json()
            if response.status == 204:
                await callback.message.answer("Success✅")
            else:
                await callback.message.answer(str(response_data))
