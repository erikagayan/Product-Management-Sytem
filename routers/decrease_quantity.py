import crud
import schemas
from fastapi import APIRouter
from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException


router = APIRouter()


@router.put("/products/decrease/{product_id}", response_model=schemas.Product, operation_id="decrease_product_quantity")
def decrease_product_quantity(product_id: int, quantity: int, db: Session = Depends(get_db)):
    updated_product = crud.decrease_product_quantity(db, product_id, quantity)

    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product
