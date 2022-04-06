from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.cancel_kb import cancel
from models.conference import Conference
from utils.get_conferences import get_conferences


class FSMDeleteConfDirector(StatesGroup):
    title_conf = State()


async def start_delete_conf(callback: types.CallbackQuery):
    try:
        if Conference.objects.count() == 0:
            await callback.message.answer(
                "Еще нет ни одной конференции, прежде чем удалить."
            )
        else:
            await FSMDeleteConfDirector.title_conf.set()
            await callback.message.answer(
                f"Конференции:\n\n{get_conferences()}\n\n"
                "Введите название конференции, "
                "чтобы удалить"
                "(достаточно начало названия)",
                reply_markup=cancel
                )
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка с началом удаления конференции."
            "Попробуйте еще раз или отмените.",
            reply_markup=cancel
        )


async def delete_conf(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["title_conf"] = message.text
        Conference.objects.filter(
            title__startswith=data["title_conf"]).first().delete()
        await message.answer("Конференция успешно удалена!")
        await state.finish()
    except Exception as error:
        print(error)
        await state.finish()
        await message.answer(
            "Произошла ошибка с удалением конференции."
        )
