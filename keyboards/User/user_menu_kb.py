from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

#
DnevnikButton = KeyboardButton(
    text="Что задано? 🤔"
)
SubscribesConfButton = KeyboardButton(
    text="Подписки 👨‍💻"
)
ConfButton = KeyboardButton(
    text="Посмотреть конференции 🗣️"
    )
Links = KeyboardButton(text="Ссылки на каналы 🧐")
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

menu_keyboard.row(DnevnikButton, SubscribesConfButton).row(ConfButton, Links)
