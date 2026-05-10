from django.contrib import admin
from .models import Category, Product

# Custom admin action
def mark_out_of_stock(modeladmin, request, queryset):
    queryset.update(stock=0, is_available=False)

mark_out_of_stock.short_description = 'Mark selected products as out of stock'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock', 'is_available']
    search_fields = ['name', 'category__name']
    list_filter = ['category', 'is_available']
    actions = [mark_out_of_stock]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']