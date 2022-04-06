from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.cancel_kb import cancel
from models.classroom import ClassRoom


class FSMCreateClass(StatesGroup):
    name = State()
    code = State()
    admin_code = State()


async def start_create_class(callback: types.CallbackQuery):
    """Callback: plusClass, начало создания классов"""
    try:
        await FSMCreateClass.name.set()
        await callback.message.answer(
            "Как назовем новый класс?",
            reply_markup=cancel
        )
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка с вызовом функции создания класса."
        )


async def create_name_class(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["name"] = message.text.lower()
        if ClassRoom.objects.filter(name=data["name"]).first() is not None:
            await message.answer("Имя для класса должно быть уникальным.")
        else:
            await FSMCreateClass.code.set()
            await message.answer(
                "Нужно задать пароль для "
                "идентификации пользователей",
                reply_markup=cancel
                )
    except Exception as error:
        print(error)
        await state.finish()
        await message.answer(
            "Произошла ошибка с началом задания имени класса."
            )


async def create_code_class(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["code"] = message.text
        if ClassRoom.objects.filter(code=data["code"]).first() is not None:
            await message.answer("Такой пароль уже существуют.\n"
                                 "Пароли должны быть уникальными.")
        else:
            await FSMCreateClass.admin_code.set()
            await message.answer(
                "А теперь нужно задать пароль администратора.",
                reply_markup=cancel
            )
    except Exception as error:
        print(error)
        await state.finish()
        await message.answer(
            "Произошла ошибка с заданием кода в процессе создания класса."
            "Попробуйте еще раз или отмените.",
            reply_markup=cancel
        )


async def create_admin_code_class(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["admin_code"] = message.text
        if ClassRoom.objects.filter(
                admin_code=data["admin_code"]).first() is not None:
            await message.answer(
                "Пароль администратора должен быть уникальным."
            )
        else:
            ClassRoom.objects.create(
                name=data["name"],
                code=data["code"],
                admin_code=data["admin_code"]
            )
            await message.answer("Класс был успешно создан!")
            await state.finish()
    except Exception as error:
        print(error)
        await message.answer(
            "Произошла ошибка в процессе создания класса на последнем этапе."
            "Попробуйте еще раз или отмените.",
            reply_markup=cancel
        )
