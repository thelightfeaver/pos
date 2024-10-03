from peewee import *
from .database import db
from .product import Product
from .user import User


class Sell(Model):
    id = AutoField()
    user = ForeignKeyField(User, backref="sells")
    total = DecimalField()
    date = DateField()
    payment = CharField()
    itbis = DecimalField(default=0)
    deleted = BooleanField(default=False)

    class Meta:
        database = db
