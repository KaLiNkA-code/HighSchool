from aiogram import Dispatcher

from .start import command_start


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(
        command_start, commands=["start"]
    )
