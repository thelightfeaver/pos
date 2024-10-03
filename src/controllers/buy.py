import datetime
from src.models.product import Product
from src.models.user import User
from src.models.buy import Buy
from src.models.buydetail import BuyDetail


def buy_products(user_id, products, total, itbis, provider, payment):
    try:
        buy = Buy.create(
            user=user_id,
            total=total,
            date=datetime.now(),
            provider=provider,
            payment=payment, 
        )
        buy.save()
        for product in products:
            product = Product.get(Product.id == product)
            buy_detail = BuyDetail.create(
                buy=buy, quantity=product.quantity, price=product.price, product=product.id, itbis=itbis
            )
            buy_detail.save()
        return buy
    except Exception as e:
        print(f"An error occurred while buying the product: {e}")
        return None
