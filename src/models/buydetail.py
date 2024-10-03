from peewee import *
from .database import db
from .buy import Buy
from .product import Product


class BuyDetail(Model):
    id = AutoField()
    buy = ForeignKeyField(Buy, backref="details")
    quantity = IntegerField()
    price = DecimalField()
    product = ForeignKeyField(Product, backref="details")
    itbis = DecimalField(default=0)

    class Meta:
        database = db
