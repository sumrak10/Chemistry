from django.shortcuts import render

from .models import Category, Product

def index(request):
    category_str = Category.objects.get(id=1)
    products = Product.objects.filter(category = category_str)

    response = render(request, "index.html", {"products": products, "category": category_str})
    return response