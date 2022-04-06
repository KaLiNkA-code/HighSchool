from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.cancel_kb import cancel
from models.user import User


class FSMNewPassword(StatesGroup):
    new_password = State()


async def start_change_password(message: types.Message):
    try:
        await FSMNewPassword.new_password.set()
        await message.answer(
            "Введите новый код для беседы:",
            reply_markup=cancel
        )
    except Exception as error:
        print(error)


async def change_password(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["new_code"] = message.text
        user = User.objects.get(uid=message.from_user.id)
        user.classroom.update(code=data["new_code"])
        await message.answer("Код успешно изменен!")
        await state.finish()
    except Exception as error:
        print(error)
