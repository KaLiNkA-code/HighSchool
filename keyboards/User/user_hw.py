from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

HomeWorkMenu = InlineKeyboardMarkup()
HW1 = InlineKeyboardButton(text='Понедельник', callback_data='hw1')
HW2 = InlineKeyboardButton(text='Вторник', callback_data='hw2')
HW3 = InlineKeyboardButton(text='Среда', callback_data='hw3')
HW4 = InlineKeyboardButton(text='Четверг', callback_data='hw4')
HW5 = InlineKeyboardButton(text='Пятница', callback_data='hw5')
HomeWorkMenu.add(HW1, HW2, HW3, HW4, HW5)
