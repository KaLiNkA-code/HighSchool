from datetime import datetime as dt

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.cancel_kb import cancel
from models.conference import Conference


class FSMConfRegister(StatesGroup):
    conf_topic = State()
    description = State()
    date = State()


async def enter_conf_topic(callback: types.Message):
    try:
        await FSMConfRegister.conf_topic.set()
        await callback.message.answer(
            'Введите название конференции.',
            reply_markup=cancel
        )
    except Exception as error:
        print(error)
        await callback.emessage.answer(
            "Произошла ошибка с вводом названия конференции."
            "Попробуйте еще раз или отмените.",
            reply_markup=cancel
        )


async def enter_description(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["title"] = message.text

        await message.answer(
            "Введите описание конференции.", reply_markup=cancel)
        await FSMConfRegister.next()
    except Exception as error:
        print(error)
        state.finish()
        await message.answer(
            "Произошла ошибка с вводом заголовка конференции."
            "Попробуйте еще раз или отмените.",
            reply_markup=cancel
        )


async def enter_date(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["description"] = message.text

        await message.answer(
            "Введите дату вот в таком формате: 23.07.2022 13:45 "
            " (день.месяц.год час:минуты)",
            reply_markup=cancel
        )
        await FSMConfRegister.next()
    except Exception as error:
        print(error)
        await message.answer(
            "Произошла ошибка с вводом описания конференции."
            "Попробуйте еще раз или отмените.",
            reply_markup=cancel
        )


async def create_conf(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["date"] = dt.strptime(message.text, "%d.%m.%Y %H:%M")

        if data["date"] < dt.today():
            await message.answer(
                "Убедитесь, что ввели верную дату. "
                "Попробуйте еще раз или отмените",
                reply_markup=cancel
            )
        else:
            Conference.objects.create(
                title=data["title"],
                description=data["description"],
                date=data["date"]
            )
            await message.answer("Конференция успешно создана!")
            await state.finish()
    except Exception as error:
        print(error)
        await message.answer(
            "Ошибка с вводом времени. Попробуйте еще раз.",
            reply_markup=cancel
            )
