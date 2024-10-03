from peewee import *
from .database import db


class User(Model):

    id = AutoField()
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
