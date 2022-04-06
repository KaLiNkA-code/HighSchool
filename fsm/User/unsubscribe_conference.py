from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.cancel_kb import cancel
from models.conference import Conference
from models.user import User


class FSMDeleteConf(StatesGroup):
    conf_title = State()


async def start_delete_conf(callback: types.CallbackQuery):
    try:
        await FSMDeleteConf.conf_title.set()
        await callback.message.answer(
            "Введите название конференции. "
            "Начала названия будет достаточно, если оно уникально.",
            reply_markup=cancel
        )
    except Exception as error:
        print(error)
        await callback.message.answer(
            "Произошла ошибка с отпиской на конференцию."
        )


async def delete_conf(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["title_conf"] = message.text
        user = User.objects.get(uid=message.from_user.id)
        conference = Conference.objects.filter(
            title__startswith=data["title_conf"]).first()
        if conference is None:
            await message.answer(
                "Данной конференции не существует, пожалуйста, "
                "попробуйте еще раз или отмените.",
                reply_markup=cancel
            )
        elif conference is not None and conference in user.conferences:
            user.conferences.remove(conference)
            conference.pupils.remove(user)
            user.save()
            conference.save()
            await message.answer(
                f"Вы отписались от {conference.title}"
            )
            await state.finish()
        else:
            await message.answer(
                "Вы не подписаны на данную конференцию. "
                "Попробуйте еще раз или отмените",
                reply_markup=cancel
            )
    except Exception as error:
        print(error)
        await state.finish()
        await message.answer(
            "Произошла ошибка с удалением конференции"
        )
