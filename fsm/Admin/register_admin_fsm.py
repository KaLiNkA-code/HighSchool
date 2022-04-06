from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from .add_homework import (FSMCreatehomework, create_homework, select_day,
                           start_create_homework)
from .change_password import (FSMNewPassword, change_password,
                              start_change_password)


def register_admin_fsm(dp: Dispatcher):
    dp.register_message_handler(
        start_change_password, text="Поменять пароль группы", state=None
    )
    dp.register_message_handler(
        start_create_homework, text="Записать домашнее задание", state=None
    )
    dp.register_callback_query_handler(
        select_day, Text(
            equals=[
                "СоздатьДЗПонедельник",
                "СоздатьДЗВторник",
                "СоздатьДЗСреда",
                "СоздатьДЗЧетверг",
                "СоздатьДЗПятница"]
                ),
        state=FSMCreatehomework.day
    )
    dp.register_message_handler(
        create_homework,
        state=FSMCreatehomework.text
    )
    dp.register_message_handler(
        change_password,
        state=FSMNewPassword.new_password
    )
