from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ConfD = InlineKeyboardMarkup(row_width=1)
plusconfDir = InlineKeyboardButton(
    text='Добавить конф.', callback_data='plusConf')
minusconfDir = InlineKeyboardButton(
    text='Удалить конф.', callback_data='minusConf')
allconfDir = InlineKeyboardButton(
    text='Все конференции', callback_data='allConf')
ConfD.add(plusconfDir, minusconfDir, allconfDir)
