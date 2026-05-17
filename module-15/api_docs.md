# ToriloShop API Documentation

## Base URL
http://127.0.0.1:8000/api/

## Authentication
This API uses JWT (JSON Web Token) authentication.
To get a token:
- POST to /api/token/ with username and password
- Use the access token in the Authorization header:
  Authorization: Bearer <your_access_token>

---

## Endpoints

### Authentication

| Method | URL | Auth Required | Description |
|--------|-----|--------------|-------------|
| POST | /api/token/ | No | Get JWT access and refresh tokens |
| POST | /api/token/refresh/ | No | Refresh access token |

#### Request Body for /api/token/
```json
{
    "username": "iyiade",
    "password": "Adebimpe@08"
}
```

#### Response
```json
{
    "access": "eyJ...",
    "refresh": "eyJ..."
}
```

---

### Products

| Method | URL | Auth Required | Description |
|--------|-----|--------------|-------------|
| GET | /api/products/ | No | List all products (paginated) |
| POST | /api/products/ | Yes | Create a new product |
| GET | /api/products/<id>/ | No | Get a single product |
| PUT | /api/products/<id>/ | Yes (creator only) | Update a product |
| DELETE | /api/products/<id>/ | Yes (creator only) | Delete a product |

#### Query Parameters for GET /api/products/
- `?search=laptop` — Search by name
- `?category=1` — Filter by category ID
- `?is_available=true` — Filter by availability
- `?ordering=price` — Order by price ascending
- `?ordering=-price` — Order by price descending
- `?page=2` — Go to page 2

#### Request Body for POST/PUT
```json
{
    "name": "Laptop",
    "price": "150000.00",
    "stock": 10,
    "category_id": 1,
    "is_available": true
}
```

---

### Categories

| Method | URL | Auth Required | Description |
|--------|-----|--------------|-------------|
| GET | /api/categories/ | No | List all categories with product count |

---

## Pagination Response Format
```json
{
    "count": 10,
    "next": "http://127.0.0.1:8000/api/products/?page=2",
    "previous": null,
    "results": [...]
}
```