import crud
import schemas
from fastapi import APIRouter
from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException


router = APIRouter()


@router.put("/products/{product_id}", response_model=schemas.Product, operation_id="update_product")
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product)

    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product
