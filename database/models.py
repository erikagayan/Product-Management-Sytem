from datetime import datetime
from database.engine import Base
from sqlalchemy import Column, Integer, String, Date, Float


class DBProduct(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(511), nullable=False)
    price = Column(Float)
    quantity = Column(Integer, default=0)
    created_at = Column(Date, default=datetime.utcnow)
