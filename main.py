import crud
import schemas
from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from routers import get_product_by_id, create_product, update_product, delete_product


app = FastAPI()

app.include_router(get_product_by_id.router)
app.include_router(create_product.router)
app.include_router(update_product.router)
app.include_router(delete_product.router)
