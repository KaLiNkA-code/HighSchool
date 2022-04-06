from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Command


from aiogram import types
bot = Bot(token='5171369020:AAEZ-Mn2C5PkfCOMHpp87Mw-rbDtp5ey6w0')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class FSMClassRegister(StatesGroup):
   class_name = State()  # 9A or 11V
   password_for_admin = State()
   default_password_for_user = State()


@dp.message_handler(Command("test"), state=None)
async def enter_class_name(message: types.Message):
    await message.answer('Введите название класса, с большой, русской буквой. Примеры:\n 9А, 11Б, 10Д')
    await FSMClassRegister.class_name.set()


@dp.message_handler(state=FSMClassRegister.class_name)
async def enter_password_for_admin(message: types.Message, state: FSMContext):
    answer1 = message.text
    async with state.proxy() as data:
        data["class_name"] = answer1

    await message.answer('Введите пароль, который будет использовать админ при входе в систему:')
    await FSMClassRegister.next()


@dp.message_handler(state=FSMClassRegister.password_for_admin)
async def enter_password_for_admin(message: types.Message, state: FSMContext):
    answer2 = message.text
    async with state.proxy() as data:
        data["password_for_admin"] = answer2

    await message.answer('Введите пароль, который будут использовать школьники при входе в систему:')
    await FSMClassRegister.next()


@dp.message_handler(state=FSMClassRegister.default_password_for_user)
async def enter_password_for_admin(message: types.Message, state: FSMContext):
    default_password_for_user = message.text
    data = await state.get_data()
    class_name = data.get("class_name")
    password_for_admin = data.get("password_for_admin")
    await message.answer(f'Класс создан. \nНазвание: {class_name}\nПароль админа: {password_for_admin}\n'
                         f'Пароль класса: {default_password_for_user}')
    await state.finish()


#  Начало загрузки нового пункта диалогового окна
# @db.message_handler(commands='load', state=None)
# async def fms_add_class_start(message: types.Message):
#     await FSMAddClass.clas.set()
#     await message.reply('Введите название класса')
#
#
# async def fsm_set_password_admin(message: types.Message, state: )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
