from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from dependencies import get_db


router = APIRouter()


@router.post("/categories/", response_model=schemas.Category, operation_id="create_category")
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)
