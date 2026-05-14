from django.urls import path
from . import api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Product endpoints
    path('products/', api_views.product_list_api, name='api_product_list'),
    path('products/<int:pk>/', api_views.product_detail_api, name='api_product_detail'),

    # Category endpoints
    path('categories/', api_views.category_list_api, name='api_category_list'),

    # JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]