from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MainMenuADMIN = ReplyKeyboardMarkup()
CheckSubscribesConf = KeyboardButton(
    text="Подписки 👨‍💻"
)
ConfButton = KeyboardButton(
    text="Посмотреть конференции 🗣️")
HomeWorkADMIN = KeyboardButton(
    text="Записать домашнее задание")
PasswordADMIN = KeyboardButton(
    text="Поменять пароль группы")
CheckHomework = KeyboardButton(
    text="Что задано? 🤔"
)

(
    MainMenuADMIN
    .add(HomeWorkADMIN)
    .add(CheckSubscribesConf, CheckHomework)
    .add(ConfButton, PasswordADMIN)
)
