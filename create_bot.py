import os

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv

from fsm.Admin.register_admin_fsm import register_admin_fsm
from fsm.Director.register_director_fsm import register_director_fsm
from fsm.register_other_fsm import register_other_fsm
from fsm.User.register_user_fsm import register_user_fsm
from handlers.Director.register_director_handlers import \
    register_director_handlers
from handlers.register_other_handlers import register_other_handlers
from handlers.User.register_user_handlers import register_user_handlers

load_dotenv()

# Получение токена
token = os.getenv("TOKEN")
mongo_host = os.getenv("MONGOHOST")

# Регистрация бота
bot = Bot(token)


def get_dp():
    dp = Dispatcher(bot, storage=MemoryStorage())

    """Other"""
    register_other_fsm(dp)
    register_other_handlers(dp)

    """Admin"""
    register_admin_fsm(dp)

    """Director"""
    register_director_handlers(dp)
    register_director_fsm(dp)

    """User"""
    register_user_fsm(dp)
    register_user_handlers(dp)

    return dp
