from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.cancel_kb import cancel
from models.classroom import ClassRoom
from utils.get_classes import get_classes


class FSMDeleteClassRoom(StatesGroup):
    classroom_name = State()


async def start_delete_classroom(callback: types.CallbackQuery):
    """Callback: minusClass, удаляем класс"""
    try:
        if ClassRoom.objects.count() == 0:
            await callback.message.answer(
                "Ни одного класса еще не было создано."
            )
        else:
            await FSMDeleteClassRoom.classroom_name.set()
            await callback.message.answer(
                f"Классы:\n\n{get_classes()}\n\nВведите название класса, "
                "который хотите удалить:",
                reply_markup=cancel
            )
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка во время удаления класса"
            "Попробуйте еще раз или отмените.",
            reply_markup=cancel
            )


async def delete_classroom(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["name_to_del"] = message.text.lower()
        classroom = ClassRoom.objects.filter(name=data["name_to_del"]).first()
        if classroom is None:
            await message.answer(
                "Введенного класса не существует. "
                "Попробуйте еще раз или отмените",
                reply_markup=cancel)
        else:
            classroom.delete()
            await message.answer("Класс успешно удален!")
            await state.finish()
    except Exception as error:
        await state.finish()
        print(error)
