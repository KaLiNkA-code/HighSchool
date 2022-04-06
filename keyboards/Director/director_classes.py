from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ClassD = InlineKeyboardMarkup(row_width=1)
plusClassDir = InlineKeyboardButton(
    text='Добавить класс', callback_data='plusClass')
minusClassDir = InlineKeyboardButton(
    text='Удалить класс', callback_data='minusClass')
allClassDir = InlineKeyboardButton(
    text='Все классы', callback_data='allClass')
ClassD.add(plusClassDir, minusClassDir, allClassDir)
