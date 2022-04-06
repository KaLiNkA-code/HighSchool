from aiogram import types

from keyboards.Director.director_classes import ClassD
from models.user import User


async def Class_call_Director(message: types.Message):
    try:
        if User.objects.get(uid=message.from_user.id).is_director:
            await message.answer('Классы: ', reply_markup=ClassD)
        else:
            await message.answer("У вас нет прав на данное действие")
    except Exception as error:
        print(error)
