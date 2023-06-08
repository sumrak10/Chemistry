from django.contrib import admin

from .models import Category, Product, Basket

# Register your models here.

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ['name']
    list_filter = ['name', 'price']