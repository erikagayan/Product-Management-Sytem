import crud
import schemas
from fastapi import Depends
from fastapi import APIRouter
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/products/", response_model=schemas.Product, operation_id="create_product")
def create_product(product: schemas.ProductCreate, database: Session = Depends(get_db)):
    return crud.create_product(database, product)
