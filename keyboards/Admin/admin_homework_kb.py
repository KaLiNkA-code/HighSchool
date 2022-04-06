from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

HomeWorkMenuA = InlineKeyboardMarkup()
HWA1 = InlineKeyboardButton(
    text='Понедельник', callback_data='СоздатьДЗПонедельник')
HWA2 = InlineKeyboardButton(text='Вторник', callback_data='СоздатьДЗВторник')
HWA3 = InlineKeyboardButton(text='Среда', callback_data='СоздатьДЗСреда')
HWA4 = InlineKeyboardButton(text='Четверг', callback_data='СоздатьДЗЧетверг')
HWA5 = InlineKeyboardButton(text='Пятница', callback_data='СоздатьДЗПятница')
HWACancel = InlineKeyboardButton(text="Отменить", callback_data="Cancel")
HomeWorkMenuA.add(HWA1, HWA2, HWA3, HWA4, HWA5).add(HWACancel)
