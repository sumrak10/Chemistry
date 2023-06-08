from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Category, Product, Basket, ProductInModel

def index(request):
    categories = Category.objects.all()

    response = render(request, "index.html", {"categories": categories})
    return response

def category(request, id:int):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    response = render(request, "category.html", {"category":category, "products": products})
    return response

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        product_id = request.POST["product_id"]
        count = request.POST["count"]
        product = Product.objects.get(id=product_id)
        basket = Basket.objects.get(id=user_id)
        pib = ProductInModel()
        pib.product = product
        pib.basket
        return JsonResponse({"message":"added"})