import logging
import asyncio

from aiogram.utils import executor
from mongoengine import connect
from utils.notifications import notifications

from create_bot import get_dp, mongo_host


def main():
    logging.info("Поехали!")

    # Подключение к базе данных
    #  connect(host=mongo_host)
    connect("f", host="localhost", port=27017)
    # connect("SchoolBotDB", host="localhost", port=27017)

    dp = get_dp()
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(notifications()),
        ioloop.create_task(executor.start_polling(dp)),
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()


if __name__ == "__main__":
    main()
