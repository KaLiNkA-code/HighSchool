from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Command


from aiogram import types
# bot = Bot(token='5171369020:AAEZ-Mn2C5PkfCOMHpp87Mw-rbDtp5ey6w0')
# dp = Dispatcher(bot, storage=MemoryStorage())
# logging.basicConfig(level=logging.INFO)


class FSMConfRegister(StatesGroup):
   conf_topic = State()  # 9A or 11V
   description = State()
   date = State()
   time = State()


# @dp.message_handler(Command("test"), state=None)
async def enter_conf_topic(message: types.Message):
    await message.answer('Введите название конференции')
    await FSMConfRegister.conf_topic.set()


# @dp.message_handler(state=FSMConfRegister.conf_topic)
async def enter_description(message: types.Message, state: FSMContext):
    answer1 = message.text
    async with state.proxy() as data:
        data["title"] = answer1

    await message.answer('Введите описание конференции')
    await FSMConfRegister.next()


# @dp.message_handler(state=FSMConfRegister.description)
async def enter_date(message: types.Message, state: FSMContext):
    answer2 = message.text
    async with state.proxy() as data:
        data["description"] = answer2

    await message.answer('Введите дату вот в таком формате: 2022-06-23  (год.месяц.день)')
    await FSMConfRegister.next()


# @dp.message_handler(state=FSMConfRegister.date)
async def enter_time(message: types.Message, state: FSMContext):
    answer3 = message.text
    async with state.proxy() as data:
        data["date"] = answer3

    await message.answer('Введите время, когда начнется конференция в формате:  13:45')
    await FSMConfRegister.next()


# @dp.message_handler(state=FSMConfRegister.time)
async def enter_password_for_admin(message: types.Message, state: FSMContext):
    time = message.text
    data = await state.get_data()
    topic = data.get("title")
    description = data.get("description")
    date = data.get('date')
    await message.answer(f'Конференция создана. \nНазвание: {topic}\nОписание: {description}\n'
                         f'Дата: {date}\nВремя: {time}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
