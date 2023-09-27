from fastapi import FastAPI
from routers import (
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
    increase_quantity,
    decrease_quantity
)


app = FastAPI()

app.include_router(get_product_by_id.router)
app.include_router(create_product.router)
app.include_router(update_product.router)
app.include_router(delete_product.router)
app.include_router(increase_quantity.router)
app.include_router(decrease_quantity.router)
