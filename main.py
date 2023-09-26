from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from dependencies import get_db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, database: Session = Depends(get_db)):
    product = crud.get_all_products(database, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product