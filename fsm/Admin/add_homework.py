from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.Admin.admin_homework_kb import HomeWorkMenuA
from keyboards.cancel_kb import cancel
from models.user import User


class FSMCreatehomework(StatesGroup):
    day = State()
    text = State()


async def start_create_homework(message: types.Message):
    try:
        if User.objects.get(uid=message.from_user.id).is_admin:
            await FSMCreatehomework.day.set()
            await message.answer(
                "На какой день запишем домашнее задание?)",
                reply_markup=HomeWorkMenuA
            )
        else:
            await message.answer("У вас нет прав на данное действие.")
    except Exception as error:
        print(error)


async def select_day(callback: types.CallbackQuery, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["day"] = callback.data.split("СоздатьДЗ")[-1]
        await FSMCreatehomework.text.set()
        await callback.message.answer(
            "А что у нас будет задано?",
            reply_markup=cancel
        )
    except Exception as error:
        print(error)


async def create_homework(message: types.Message, state: FSMContext):
    try:
        user = User.objects.get(uid=message.from_user.id)
        if user.is_admin:
            async with state.proxy() as data:
                data["homework"] = message.text
            user.classroom.homeworks[data["day"]] = data["homework"]
            user.classroom.save()
            await message.answer("Запись успешно создана!")
        else:
            await message.answer("У вас нет прав на данное действие.")
        await state.finish()
    except Exception as error:
        print(error)
