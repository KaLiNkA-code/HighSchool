from aiogram.types import InlineKeyboardMarkup, KeyboardButton

NewsButton = KeyboardButton(
    text='Новости',
    url='https://t.me/HighSchoolNewsKaLiNkATeam'
)
INTMARButton = KeyboardButton(
    text='Интеллектуальный марафон',
    url='https://t.me/HighSchoolIntellectualMarathon'
)
OSMCHTENButton = KeyboardButton(
    text='Осмысленное чтение',
    url='https://t.me/HighSchoolMeaningfulReadingKLNK'
)

LinksKeyboardMarkup = InlineKeyboardMarkup()
LinksKeyboardMarkup.add(NewsButton, INTMARButton, OSMCHTENButton)
