from peewee import *
from .database import db
from .product import Product
from .sell import Sell


class SellDetail(Model):
    id = AutoField()
    sell = ForeignKeyField(Sell, backref="details")
    quantity = IntegerField()
    price = DecimalField()
    product = ForeignKeyField(Product, backref="details")
    itbis = DecimalField(default=0)

    class Meta:
        database = db
