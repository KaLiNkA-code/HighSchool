from mongoengine.document import Document
from mongoengine.fields import (BooleanField, IntField, ListField,
                                ReferenceField, StringField)

from .classroom import ClassRoom


class User(Document):
    uid = IntField(required=True)

    username = StringField()
    first_name = StringField()
    last_name = StringField()

    is_director = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    classroom = ReferenceField(ClassRoom, CASCADE=True)
    conferences = ListField(
        ReferenceField("Conference", CASCADE=True), default=[])
