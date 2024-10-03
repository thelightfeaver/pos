from peewee import *
from .database import db
from .user import User


class Buy(Model):
    id = AutoField()
    user = ForeignKeyField(User, backref="buys")
    total = DecimalField()
    date = DateField()
    provider = CharField()
    payment = CharField()
    deleted = BooleanField(default=False)

    class Meta:
        database = db
