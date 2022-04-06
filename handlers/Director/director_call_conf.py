from aiogram import types

from keyboards.Director.director_change_conf import ConfD
from models.user import User


async def Conf_call_Director(message: types.Message):
    try:
        if User.objects.get(uid=message.from_user.id).is_director:
            await message.answer('Конференции: ', reply_markup=ConfD)
        else:
            await message.answer("У вас нет прав на данное действие.")
    except Exception as error:
        print(error)
