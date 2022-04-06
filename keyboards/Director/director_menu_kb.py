from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MainMenuDir = ReplyKeyboardMarkup(row_width=1)
ConfDir = KeyboardButton(
    text='Конференции', callback_data='ConfDir')
ClassDir = KeyboardButton(
    text='Классы', callback_data='ClassDir')
MainMenuDir.add(ConfDir, ClassDir)
