from aiogram import Dispatcher

from .subscribe_conference import (FSMSubscribeConf, start_subscribe_conf,
                                   subscribe_conf)
from .unsubscribe_conference import (FSMDeleteConf, delete_conf,
                                     start_delete_conf)


def register_user_fsm(dp: Dispatcher):
    dp.register_callback_query_handler(
        start_subscribe_conf, text="SubscribeConf"
    )
    dp.register_message_handler(
        subscribe_conf, state=FSMSubscribeConf.conf_title
    )
    dp.register_callback_query_handler(
        start_delete_conf, text="UnsubscribeConf"
    )
    dp.register_message_handler(
        delete_conf, state=FSMDeleteConf.conf_title
    )
