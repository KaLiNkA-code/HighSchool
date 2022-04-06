from aiogram import types

from utils.get_classes import get_classes
from models.classroom import ClassRoom


async def check_classrooms(callback: types.CallbackQuery):
    """Callback: allClass, Возвращаем в str список классов."""
    try:
        if ClassRoom.objects.count() == 0:
            await callback.message.answer(
                "На данный момент нет классов."
            )
        else:
            await callback.message.answer("Классы: \n\n" + get_classes())
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка с формированием классов =("
            )
