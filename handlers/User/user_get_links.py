from aiogram import types

from keyboards.User.user_links import LinksKeyboardMarkup


async def get_links(message: types.Message):
    await message.answer(
        "Ссылки:",
        reply_markup=LinksKeyboardMarkup
    )
