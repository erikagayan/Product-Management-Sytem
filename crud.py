from datetime import datetime

from sqlalchemy.orm import Session
from database.models import DBProduct
from schemas import ProductCreate, ProductUpdate


def datetime_to_str(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_all_products(database: Session, product_id: int):
    product = database.query(DBProduct).filter(DBProduct.id == product_id).first()

    if product:
        product.created_at = datetime_to_str(product.created_at)

    return product
