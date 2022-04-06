from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="Отменить", callback_data="Cancel")
)
