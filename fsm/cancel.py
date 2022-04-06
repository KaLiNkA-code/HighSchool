from aiogram import types
from aiogram.dispatcher import FSMContext


async def cancel_state(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.message.answer("Отменено!")
