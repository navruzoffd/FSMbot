from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from src.states.base import (
    CreateAlertState
)
from src.handlers.base_handlers import (
    set_5m_volume_change,
    set_age,
    set_ignore_social_networks,
    set_marketcap,
    set_tx1d,
    set_tx1h,
    set_tx5m,
    start,
    create_alert,
    submit_alert_request,
)
from src.handlers.state import (
    state_5m_volume_change,
    state_age,
    state_ignore_social_networks,
    state_marketcap,
    state_title_and_filters,
    state_tx1d,
    state_tx1h,
    state_tx5m
)


def register_handlers(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.callback_query.register(start, lambda c: c.data =="start")

    
    router.callback_query.register(create_alert, lambda c: c.data == "create")
    router.callback_query.register(set_age, lambda c: c.data == "state_age")
    router.callback_query.register(set_marketcap, lambda c: c.data == "state_marketcap")
    router.callback_query.register(set_ignore_social_networks, lambda c: c.data == "state_ingnore_social")
    router.callback_query.register(set_5m_volume_change, lambda c: c.data == "5m_volume_change")
    router.callback_query.register(set_tx1d, lambda c: c.data == "tx1d")
    router.callback_query.register(set_tx1h, lambda c: c.data == "tx1h")
    router.callback_query.register(set_tx5m, lambda c: c.data == "tx5m")
    router.callback_query.register(submit_alert_request, lambda c: c.data == "submit_alert")
    # router.callback_query.register(..., lambda c: c.data == "view")
    # router.callback_query.register(..., lambda c: c.data == "delete")


    router.message.register(state_title_and_filters, CreateAlertState.title)
    router.message.register(state_age, CreateAlertState.age_range)
    router.message.register(state_marketcap, CreateAlertState.marketcap_range)
    router.message.register(state_ignore_social_networks, CreateAlertState.ignore_social_networks)
    router.message.register(state_5m_volume_change, CreateAlertState.m5_volume_change)
    router.message.register(state_tx1d, CreateAlertState.tx1d)
    router.message.register(state_tx1h, CreateAlertState.tx1h)
    router.message.register(state_tx5m, CreateAlertState.tx5m)

    # router.message.register(state_message, MessageState.text)