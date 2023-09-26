from datetime import datetime

from sqlalchemy.orm import Session
from database.models import DBProduct
from schemas import ProductCreate, ProductUpdate


def get_all_products(database: Session, product_id: int):
    return database.query(DBProduct).filter(DBProduct.id == product_id).first()


def create_product(database: Session, product: ProductCreate):
    database_product = DBProduct(**product.model_dump())
    database.add(database_product)
    database.commit()
    database.refresh(database_product)
    return database_product
