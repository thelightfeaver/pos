from .user import User
from .product import Product
from .buy import Buy
from .buydetail import BuyDetail
from .sell import Sell
from .selldetail import SellDetail
from .database import db

db.create_tables([User, Product, Buy, BuyDetail, Sell, SellDetail])
