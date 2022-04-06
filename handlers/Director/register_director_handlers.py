from aiogram import Dispatcher

from .classrooms import check_classrooms
from .conference import get_conference_list
from .director_call_class import Class_call_Director
from .director_call_conf import Conf_call_Director


def register_director_handlers(dp: Dispatcher):
    dp.register_message_handler(
        Conf_call_Director, text="Конференции"
    )
    dp.register_message_handler(
        Class_call_Director, text="Классы"
    )
    dp.register_callback_query_handler(
        check_classrooms, text="allClass"
    )
    dp.register_callback_query_handler(
        get_conference_list, text="allConf"
    )
