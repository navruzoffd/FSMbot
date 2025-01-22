from aiogram.types import Message
from config import settings
from aiohttp import ClientSession
from aiogram.fsm.context import FSMContext
from src.keyboards.base import filters_keyboard
from src.states.base import CreateAlertState


async def state_title_and_filters(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer("Select filters:", reply_markup=filters_keyboard())

async def state_age(message: Message, state: FSMContext):
    try:
        age_range = message.text.split("-")
        age_range = [float(num)*3600 for num in age_range]
        age_range = " ".join(map(str, age_range))
        await state.update_data(age_range=age_range)
        await message.answer("Done✅")
    except Exception as e:
        await message.answer("Введите верный диапазон!")

async def state_marketcap(message: Message, state: FSMContext):
    try:
        marketcap_range = message.text.split("-")
        marketcap_range = " ".join(marketcap_range)
        await state.update_data(marketcap_range=marketcap_range)
        await message.answer("Done✅")
    except Exception as e:
        await message.answer("Введите верный диапазон!")

async def state_ignore_social_networks(message: Message, state: FSMContext):
    if message.text == "yes":
        flag = True
        await state.update_data(ignore_social_networks = flag)
        await message.answer("Done✅")
    elif message.text == "no":
        flag = False
        await state.update_data(ignore_social_networks = flag)
        await message.answer("Done✅")
    else:
        await message.answer('Введите "yes" или "no"')

async def state_5m_volume_change(message: Message, state: FSMContext):
    try:
        m5_volume_change = float(message.text)
        await state.update_data(m5_volume_change=m5_volume_change)
        await message.answer("Done✅")
    except Exception as e:
        await message.answer("Ведите число!")

async def state_tx1d(message: Message, state: FSMContext):
    try:
        tx1d = int(message.text)
        await state.update_data(tx1d=tx1d)
        await message.answer("Done✅")
    except Exception as e:
        await message.answer("Ведите число!")

async def state_tx1h(message: Message, state: FSMContext):
    try:
        tx1h = int(message.text)
        await state.update_data(tx1h=tx1h)
        await message.answer("Done✅")
    except Exception as e:
        await message.answer("Ведите число!")

async def state_tx5m(message: Message, state: FSMContext):
    try:
        tx5m = int(message.text)
        await state.update_data(tx5m=tx5m)
        await message.answer("Done✅")
    except Exception as e:
        await message.answer("Ведите число!")


    
#     text = message.text
#     data = {
#         "text": text
#     }

#     url = settings.DOMAIN + f"chats/{message.from_user.id}/messages"
#     async with ClientSession() as session:
#         async with session.post(url, json=data) as response:
#             if response.status == 200:
#                 await message.answer(f"Сообщение добавлено")
#             else:
#                 await message.answer(f"Ошибка {response.status}")