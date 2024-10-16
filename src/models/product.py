from peewee import *
from .database import db


class Product(Model):
    id = AutoField()
    name = CharField()
    description = CharField()
    price_details = DecimalField()
    date = DateField()
    price_sale = DecimalField()
    stock = IntegerField()
    itbis = DecimalField(default=0)
    deleted = BooleanField(default=False)

    class Meta:
        database = db
