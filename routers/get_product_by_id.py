import crud
import schemas
from fastapi import APIRouter
from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException


router = APIRouter()


@router.get("/products/{product_id}", response_model=schemas.Product, operation_id="get_product")
def read_product(product_id: int, database: Session = Depends(get_db)):
    product = crud.get_product_by_id(database, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product
