from aiogram import types

from keyboards.User.user_hw import HomeWorkMenu
from models.user import User


async def HomeWork_call(message: types.Message):
    await message.answer(
        'На какой день недели Вас интересует домашняя работа?',
        reply_markup=HomeWorkMenu
    )


async def get_homework(callback: types.CallbackQuery):
    try:
        user = User.objects.get(uid=callback.from_user.id)
        vrs = {
            "hw1": "Понедельник",
            "hw2": "Вторник",
            "hw3": "Среда",
            "hw4": "Четверг",
            "hw5": "Пятница"
        }
        day = callback.data
        await callback.message.answer(
            f"{vrs.get(day)}:\n\n{user.classroom.homeworks[vrs.get(day)]}"
        )
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка с формированием домашнего задания."
        )
