from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.keyboards.base import filters_keyboard


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
    except Exception:
        await message.answer("Enter valid range!")


async def state_marketcap(message: Message, state: FSMContext):
    try:
        marketcap_range = message.text.split("-")
        marketcap_range = " ".join(marketcap_range)
        await state.update_data(marketcap_range=marketcap_range)
        await message.answer("Done✅")
    except Exception:
        await message.answer("Enter valid range!")


async def state_ignore_social_networks(message: Message, state: FSMContext):
    if message.text == "yes":
        flag = True
        await state.update_data(ignore_social_networks=flag)
        await message.answer("Done✅")
    elif message.text == "no":
        flag = False
        await state.update_data(ignore_social_networks=flag)
        await message.answer("Done✅")
    else:
        await message.answer('Type "yes" or "no"')


async def state_5m_volume_change(message: Message, state: FSMContext):
    try:
        m5_volume_change = float(message.text)
        await state.update_data(m5_volume_change=m5_volume_change)
        await message.answer("Done✅")
    except Exception:
        await message.answer("Enter number!")


async def state_tx1d(message: Message, state: FSMContext):
    try:
        tx1d = int(message.text)
        await state.update_data(tx1d=tx1d)
        await message.answer("Done✅")
    except Exception:
        await message.answer("Enter number!")


async def state_tx1h(message: Message, state: FSMContext):
    try:
        tx1h = int(message.text)
        await state.update_data(tx1h=tx1h)
        await message.answer("Done✅")
    except Exception:
        await message.answer("Enter number!")


async def state_tx5m(message: Message, state: FSMContext):
    try:
        tx5m = int(message.text)
        await state.update_data(tx5m=tx5m)
        await message.answer("Done✅")
    except Exception:
        await message.answer("Enter number!")
