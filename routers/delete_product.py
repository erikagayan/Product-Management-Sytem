import crud
import schemas
from . import router
from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException


@router.delete("/products/{product_id}", response_model=schemas.Product, operation_id="delete_product")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)

    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return deleted_product
