from mongoengine.document import Document
from mongoengine.fields import (DictField, ListField, ReferenceField,
                                StringField)


class ClassRoom(Document):
    __collection__ = "classroom"

    name = StringField(required=True)
    pupils = ListField(ReferenceField("User"), default=[])
    code = StringField(default="", unique=True)
    admin_code = StringField(required=True, unique=True)

    homeworks = DictField(
        default={
            "Понедельник": "Ничего не задано.",
            "Вторник": "Ничего не задано.",
            "Среда": "Ничего не задано.",
            "Четверг": "Ничего не задано.",
            "Пятница": "Ничего не задано."
        }
    )
