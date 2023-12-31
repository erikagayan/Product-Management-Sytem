# Product Management System

This is API for managing products and categories. You can create, update, delete and retrieve information about products and categories.


## Launching
```bash
1. pip install -r requirements.txt
2. alembic upgrade head
3. uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

# Using the API
## Products
### Create Product
```bash
POST /products/

Example request:
{
    "name": "New Product",
    "description": "Product description",
    "price": 19.99,
    "quantity": 100,
    "category_id": 1
}

Example response:
{
    "id": 1,
    "name": "New Product",
    "description": "Product description",
    "price": 19.99,
    "quantity": 100,
    "category_id": 1,
    "created_at": "2023-09-29T12:00:00"
}
```

### Update Product
```Bash
PUT /products/{product_id}

Example request:
{
    "name": "Updated Product",
    "price": 24.99
}

Example response:
{
    "id": 1,
    "name": "Updated Product",
    "description": "Product description",
    "price": 24.99,
    "quantity": 100,
    "category_id": 1,
    "created_at": "2023-09-29T12:00:00"
}
```


### Delete a Product
```bash
DELETE /products/{product_id}

Example response:
{
    "id": 1,
    "name": "Updated Product",
    "description": "Product description",
    "price": 24.99,
    "quantity": 100,
    "category_id": 1,
    "created_at": "2023-09-29T12:00:00"
}
```


### Get a Product by ID
```bash
GET /products/{product_id}

Example response:
{
    "id": 1,
    "name": "Updated Product",
    "description": "Product description",
    "price": 24.99,
    "quantity": 100,
    "category_id": 1,
    "created_at": "2023-09-29T12:00:00"
}
```


### Increase Product Quantity
```bash
PUT /products/increase/{product_id}?quantity=10

Example response:
{
    "id": 1,
    "name": "Updated Product",
    "description": "Product description",
    "price": 24.99,
    "quantity": 110,
    "category_id": 1,
    "created_at": "2023-09-29T12:00:00"
}
```

### Decrease Product Quantity
```bash
PUT /products/decrease/{product_id}?quantity=5

Example response:
{
    "id": 1,
    "name": "Updated Product",
    "description": "Product description",
    "price": 24.99,
    "quantity": 105,
    "category_id": 1,
    "created_at": "2023-09-29T12:00:00"
}
```


## Categories
### Create a Category
```bash
POST /categories/

Example request:
{
    "name": "New Category"
}

Example response:
{
    "id": 1,
    "name": "New Category"
}
```