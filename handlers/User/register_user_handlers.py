from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from .conference import check_conf, check_subscribes_conf
from .get_homework import HomeWork_call, get_homework
from .user_get_links import get_links


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(
        get_links, text="Ссылки на каналы 🧐"
    )
    dp.register_message_handler(
        HomeWork_call, text="Что задано? 🤔"
    )
    dp.register_callback_query_handler(
        get_homework, Text(equals=[
            "hw1",
            "hw2",
            "hw3",
            "hw4",
            "hw5"
        ])
    )
    dp.register_message_handler(
        check_conf, text="Посмотреть конференции 🗣️"
    )
    dp.register_message_handler(
        check_subscribes_conf, text="Подписки 👨‍💻"
    )
