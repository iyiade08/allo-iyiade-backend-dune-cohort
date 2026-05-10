# ToriloShop - Django REST API

## Project Description
ToriloShop now exposes a REST API built with Django REST Framework.
The API allows full CRUD operations on products and listing of
categories with product counts.

## Features Implemented

### Product Endpoints
- **GET** `/api/products/` — List all products
- **POST** `/api/products/` — Create a new product
- **GET** `/api/products/<id>/` — Retrieve a single product
- **PUT** `/api/products/<id>/` — Full update of a product
- **DELETE** `/api/products/<id>/` — Delete a product

### Category Endpoints
- **GET** `/api/categories/` — List all categories with product count

### Serializers
- **ProductSerializer** — All product fields with nested category object
- **CategorySerializer** — All category fields with product count
  using SerializerMethodField

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/iyiade08/allo-iyiade-backend-dune-cohort.git
2. Navigate into module-13 folder:
   cd allo-iyiade-backend-dune-cohort/module-13
3. Create virtual environment:
   python -m venv venv
4. Activate it:
   venv\Scripts\activate
5. Install dependencies:
   pip install django djangorestframework pillow
6. Run migrations:
   python manage.py migrate
7. Create superuser:
   python manage.py createsuperuser
8. Run the server:
   python manage.py runserver
9. Open Postman and import toriloshop_api_collection.json
10. Test all endpoints

## Screenshots
![Get Products](screenshots/01_get_products.png)
![Post Create Product](screenshots/02_post_create_product.png)
![Get Single Product](screenshots/03_get_single_product.png)
![Put Update Product](screenshots/04_put_update_product.png)
![Delete Product](screenshots/05_delete_product.png)
![Get Categories](screenshots/06_get_categories.png)