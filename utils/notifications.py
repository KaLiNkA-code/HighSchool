from datetime import datetime, timedelta
import asyncio

from create_bot import bot
from mongoengine.queryset.visitor import Q

from models.conference import Conference


async def notifications():
    while True:
        conferences = Conference.objects.filter(
            Q(
                date__gte=datetime.now()+timedelta(minutes=1)
            ) &
            Q(
                date__lte=datetime.now()+timedelta(minutes=500)
            )
        )
        if conferences:
            for conf in conferences:
                for user in conf.pupils:
                    await bot.send_message(
                        chat_id=user.id,
                        text=f"Конференция {conf.title} скоро "
                             "начнется, не опаздывайте!"
                    )
        await asyncio.sleep(120)
