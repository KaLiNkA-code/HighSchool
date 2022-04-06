from aiogram import types

from models.conference import Conference
from utils.get_conferences import get_conferences


async def get_conference_list(callback: types.CallbackQuery):
    try:
        if Conference.objects.count() == 0:
            await callback.message.answer(
                "На данный момент нет конференций."
            )
        else:
            await callback.message.answer(
                f"Конференции:\n{get_conferences()}"
            )
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка с формированием конференций"
        )
