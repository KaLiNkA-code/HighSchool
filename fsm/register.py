import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv

from keyboards.Admin.admin_menu_kb import MainMenuADMIN
from keyboards.cancel_kb import cancel
from keyboards.Director.director_menu_kb import MainMenuDir
from keyboards.User.user_menu_kb import menu_keyboard
from models.user import User
from utils.create_user import create_user_func

load_dotenv()


class FSMRegister(StatesGroup):
    create_user = State()


async def register_user(message: types.Message):
    try:
        await FSMRegister.create_user.set()
        if User.objects.filter(uid=message.from_user.id).first() is None:
            user_data = message.from_user
            User.objects.create(
                uid=user_data.id,
                username=user_data.username if user_data.username else "",

                first_name=user_data.first_name if
                user_data.first_name else "",

                last_name=user_data.last_name if user_data.last_name else ""
            )
        await message.answer(
            "Вы зарегистрированы, однако нужен код идентификации "
            "\n\n Пожалуйста, введите код:\n",
            reply_markup=cancel
        )
    except Exception as error:
        print(error)


async def take_code(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["code"] = message.text
        user = User.objects.get(uid=message.from_user.id)
        if data["code"] == os.getenv("DIRECTOR_PASSWORD"):
            user.is_director = True
            user.save()
            await message.answer(
                "Вы успешно были зарегистрированы! Ваш статус: Директор",
                reply_markup=MainMenuDir
            )
            await state.finish()
        else:
            status_room = await create_user_func(data, user)
            if isinstance(status_room, str):
                await message.answer(
                    "Введенный код не принадлежит ни одному классу. "
                    "Попробуйте еще раз или отмените.", reply_markup=cancel)
            else:
                await message.answer(
                    "Вы были идентифицированы!\n"
                    f"{status_room[0]} {status_room[1]}\n"
                    "Знакомство с интерфейсом:\n"
                    "'Что задано' - Вызывает меню с домашними работами\n"
                    "'Подписки' - Вызывает конференции, на которые прийдут уведомления\n"
                    "'Посмотреть конференции' - Вызывает меню конференций, на которые можно подписаться\n"
                    "'Ссылки на каналы' - ссылки на официальные каналы школы 138\n\n"
                    "На данный момент бот находится на пробном периоде. Сейчас возможны корректировки и нововведения!"
                    "Если у вас есть предложение или хотите проголосовать за поправку в этом боте: https://t.me/+5S11q8EAkBUyYmFi",
                    reply_markup=menu_keyboard if
                    status_room[0] == ("Участник группы") else MainMenuADMIN)
                await state.finish()
    except Exception as error:
        print(error)
        await message.answer(
            "Произошла ошибка. Возможно, неверный код, попробуйте еще раз."
        )
