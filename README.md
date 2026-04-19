# ToriloShop - Django Project

## Project Description

ToriloShop is a Django-based online shop built as part of the Backend Dune Cohort.
It now includes two models: Category and Product, demonstrating Django ORM,
migrations, admin registration, and shell queries.

## Features Implemented

### Models

- **Category** — fields: name (CharField), description (TextField)
- **Product** — fields: name (CharField), price (DecimalField),
  stock (IntegerField), category (ForeignKey → Category),
  created_at (DateTimeField)

### ORM Operations Performed

- Added 3 categories and 6 products using the Django shell
- Retrieved all products using `Product.objects.all()`
- Filtered products by category using `Product.objects.filter(category__name=...)`
- Filtered products with price > 5000 using `Product.objects.filter(price__gt=5000)`
- Updated one product's price and confirmed the change
- Deleted one product and confirmed the deletion
- Registered both models in the admin panel

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/iyiade08/allo-iyiade-backend-dune-cohort.git
2. Navigate into the project folder:
   cd allo-iyiade-backend-dune-cohort
3. Create a virtual environment:
   python -m venv venv
4. Activate it:
   venv\Scripts\activate
5. Install dependencies:
   pip install django
6. Run migrations:
   python manage.py migrate
7. Create a superuser:
   python manage.py createsuperuser
8. Run the server:
   python manage.py runserver
9. Open browser at `http://127.0.0.1:8000/`

## Screenshots

![Admin Panel](screenshots/01_admin_panel.png)
![Admin Categories](screenshots/01b_admin_categories.png)
![Shell Add Data](screenshots/02_shell_add_data.png)
![Shell All Products](screenshots/03_shell_all_products.png)
![Shell By Category](screenshots/04_shell_by_category.png)
![Shell Price Filter](screenshots/05_shell_price_filter.png)
![Shell Update and Delete](screenshots/06_shell_update_delete.png)
