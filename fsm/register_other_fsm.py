from aiogram import Dispatcher
from .cancel import cancel_state
from .register import FSMRegister, take_code


def register_other_fsm(dp: Dispatcher):
    """Регистрация"""
    dp.register_message_handler(take_code, state=FSMRegister.create_user)

    """Отмена"""
    dp.register_callback_query_handler(
        cancel_state, text="Cancel", state="*"
    )
