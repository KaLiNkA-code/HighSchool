# import logging
from aiogram import types

from fsm.register import register_user
from keyboards.Admin.admin_menu_kb import MainMenuADMIN
from keyboards.Director.director_menu_kb import MainMenuDir
from keyboards.User.user_menu_kb import menu_keyboard
from models.user import User


async def command_start(message: types.Message):
    try:
        user = User.objects.filter(uid=message.from_user.id).first()
        if user is None or (
            user is not None and user.is_director is False
                and user.classroom is None):
            await register_user(message)
        else:
            if user.is_director:
                await message.answer(
                    f"Здравствуйте, {user.last_name} {user.first_name}!",
                    reply_markup=MainMenuDir
                )
            elif user.is_admin:
                await message.answer(
                    "Вы уже зарегистрированы.",
                    reply_markup=MainMenuADMIN
                )
            else:
                await message.answer(
                    "Вы уже зарегистрированы.",
                    reply_markup=menu_keyboard
                )
    except Exception as error:
        print(error)
