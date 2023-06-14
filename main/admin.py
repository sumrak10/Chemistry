from django.contrib import admin

from .models import Category, Product, Basket, ProductInBasket, Order, ProductInOrder, Favorites, FavoriteProduct, Question, ChangePasswordUser

# Register your models here.


class ProductInBasketInline(admin.TabularInline):
    model = ProductInBasket

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder

class FavoriteProductInline(admin.TabularInline):
    model = FavoriteProduct

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["fio", "text"]

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ["user"]
    inlines = [FavoriteProductInline]

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user"]
    inlines = [ProductInBasketInline]

@admin.register(Order)
class OrdeerAdmin(admin.ModelAdmin):
    list_display = ["user", "date_created"]
    inlines = [ProductInOrderInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ['name']
    list_filter = ['name', 'price']

@admin.register(ChangePasswordUser)
class ChangePasswordUserAdmin(admin.ModelAdmin):
    list_display = ["user", "secret"]