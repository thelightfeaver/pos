from src.models.product import Product


def create_product(name, description, details, date, price_sale, stock, itbis):
    try:
        product = Product.create(
            name=name,
            description=description,
            details=details,
            date=date,
            price_sale=price_sale,
            stock=stock,
            itbis=itbis,
        )
        product.save()
        return product
    except Exception as e:
        print(f"An error occurred while creating the product: {e}")
        return None


def get_products():
    try:
        products = Product.select().where(Product.deleted == False)
        return products
    except Exception as e:
        print(f"An error occurred while getting the products: {e}")
        return None


def get_product_by_id(product_id):
    try:
        product = Product.select().where(
            Product.id == product_id, Product.deleted == False
        )
        return product
    except Exception as e:
        print(f"An error occurred while getting the product: {e}")
        return None


def update_product(
    product_id, name, description, details, date, price_sale, stock, itbis
):
    try:
        product = Product.get(Product.id == product_id)
        product.name = name
        product.description = description
        product.details = details
        product.date = date
        product.price_sale = price_sale
        product.stock = stock
        product.itbis = itbis
        product.save()
        return product
    except Exception as e:
        print(f"An error occurred while updating the product: {e}")
        return None
