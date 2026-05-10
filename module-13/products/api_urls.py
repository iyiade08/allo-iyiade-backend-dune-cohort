from django.urls import path
from . import api_views

urlpatterns = [
    path('products/', api_views.product_list_api, name='api_product_list'),
    path('products/<int:pk>/', api_views.product_detail_api, name='api_product_detail'),
    path('categories/', api_views.category_list_api, name='api_category_list'),
]