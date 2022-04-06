from aiogram import types

from keyboards.User.user_subscribes import subscribeMarkUp
from models.conference import Conference
from models.user import User
from utils.get_conferences import get_conferences


async def check_conf(message: types.Message):
    if Conference.objects.count() == 0:
        await message.answer(
            "На данный момент нет конференций."
        )
    await message.answer(
        f"Конференции:\n{get_conferences()}",
        reply_markup=subscribeMarkUp
    )


async def check_subscribes_conf(message: types.Message):
    try:
        user = User.objects.get(uid=message.from_user.id)
        if user.conferences:
            info = "Конференции, на которые вы подписаны:\n"
            for conf in user.conferences:
                info += f"\n{conf.title}, всего подписок {len(conf.pupils)}"
            await message.answer(
                info, reply_markup=subscribeMarkUp
            )
        else:
            await message.answer(
                "Вы еще не подписаны ни на одну конференцию. Исправим?)",
                reply_markup=subscribeMarkUp
            )
    except Exception as error:
        print(error)
        await message.answer(
            "Произошла ошибка с формированием конференций."
        )
