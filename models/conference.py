from mongoengine.document import Document
from mongoengine.fields import (DateTimeField, ListField, ReferenceField,
                                StringField)

from models.user import User


class Conference(Document):

    title = StringField(required=True)
    description = StringField(required=True)
    date = DateTimeField(required=True)
    pupils = ListField(ReferenceField(User), default=[])
