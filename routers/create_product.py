import crud
import schemas
from . import router
from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, database: Session = Depends(get_db)):
    return crud.create_product(database, product)
