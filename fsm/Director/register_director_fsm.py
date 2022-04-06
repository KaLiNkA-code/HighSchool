from aiogram import Dispatcher

from .create_classroom import (FSMCreateClass, create_admin_code_class,
                               create_code_class, create_name_class,
                               start_create_class)
from .create_conference import (FSMConfRegister, create_conf, enter_conf_topic,
                                enter_date, enter_description)
from .delete_classroom import (FSMDeleteClassRoom, delete_classroom,
                               start_delete_classroom)
from .delete_conference import (FSMDeleteConfDirector, delete_conf,
                                start_delete_conf)


def register_director_fsm(dp: Dispatcher):
    """Директор"""

    """Создание класса"""
    dp.register_callback_query_handler(
        start_create_class, text="plusClass"
    )

    dp.register_message_handler(
        create_name_class, state=FSMCreateClass.name
    )

    dp.register_message_handler(
        create_code_class, state=FSMCreateClass.code
    )

    dp.register_message_handler(
        create_admin_code_class, state=FSMCreateClass.admin_code
    )

    """Удаление класса"""
    dp.register_callback_query_handler(
        start_delete_classroom, text="minusClass"
    )

    dp.register_message_handler(
        delete_classroom, state=FSMDeleteClassRoom.classroom_name
    )

    """Добавление конференции"""

    dp.register_callback_query_handler(
        enter_conf_topic, text="plusConf"
    )

    dp.register_message_handler(
        enter_description, state=FSMConfRegister.conf_topic
    )

    dp.register_message_handler(
        enter_date, state=FSMConfRegister.description
    )

    dp.register_message_handler(
        create_conf, state=FSMConfRegister.date
    )

    """Удаление конференции"""
    dp.register_callback_query_handler(
        start_delete_conf, text="minusConf"
    )

    dp.register_message_handler(
        delete_conf, state=FSMDeleteConfDirector.title_conf
    )
