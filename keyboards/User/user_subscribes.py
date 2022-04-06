from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

subscribeMarkUp = InlineKeyboardMarkup()
subscribe = InlineKeyboardButton(
    text="Подписаться", callback_data="SubscribeConf")
unsubscribe = InlineKeyboardButton(
    text="Отписаться", callback_data="UnsubscribeConf"
)
subscribeMarkUp.add(subscribe, unsubscribe)
