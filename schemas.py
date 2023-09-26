from pydantic import BaseModel
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: str
    price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    # created_at: datetime

    class Config:
        from_attributes = True
