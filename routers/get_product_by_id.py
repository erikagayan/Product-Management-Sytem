import crud
import schemas
from . import router
from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException


@router.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, database: Session = Depends(get_db)):
    product = crud.get_all_products(database, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product
