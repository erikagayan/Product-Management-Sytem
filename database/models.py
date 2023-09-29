from datetime import datetime

from sqlalchemy.orm import relationship

from database.engine import Base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey


class DBCategory(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

    products = relationship("DBProduct", back_populates="category")


class DBProduct(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(511), nullable=False)
    price = Column(Float)
    quantity = Column(Integer, default=0)
    created_at = Column(Date, default=datetime.utcnow)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category = relationship(DBCategory, back_populates="products")
