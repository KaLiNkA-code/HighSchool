from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.cancel_kb import cancel
from models.conference import Conference
from models.user import User
from utils.get_conferences import get_conferences


class FSMSubscribeConf(StatesGroup):
    conf_title = State()


async def start_subscribe_conf(callback: types.CallbackQuery):
    try:
        await FSMSubscribeConf.conf_title.set()
        await callback.message.answer(
            f"Конференции:\n{get_conferences()}\n\n"
            "Введите название конференции, чтобы подписаться. "
            "Будет достаточно начала названия, если оно уникально",
            reply_markup=cancel
        )
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка с подпиской на конференцию."
        )


async def subscribe_conf(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["title"] = message.text
        conference = Conference.objects.filter(
            title__startswith=data["title"]).first()
        user = User.objects.get(uid=message.from_user.id)
        if conference is None:
            await message.answer(
                "Введенной конференции не найдено. "
                "Пожалуйста, попробуйте еще раз или отмените",
                reply_markup=cancel
            )
        elif conference is not None and user in conference.pupils:
            await message.answer(
                "Вы уже подписаны на данную конференцию."
            )
            await state.finish()
        else:
            conference.pupils.append(user)
            user.conferences.append(conference)
            user.save()
            conference.save()
            await message.answer(
                f"Вы подписались на {conference.title}"
            )
            await state.finish()
    except Exception as error:
        print(error)
        await message.answer(
            "Произошла ошибка с подпиской на конференцию."
        )
