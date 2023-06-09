from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse

from .models import Category, Product, Basket, ProductInModel
from .forms import UserForm

def index(request):
    categories = Category.objects.all()

    response = render(request, "index.html", {"categories": categories})
    return response

def category(request, id:int):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    response = render(request, "category.html", {"category":category, "products": products})
    return response

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            user = authenticate(username=new_user.username, password=request.POST["password"])
            login(request, user)
            return redirect("index")
    else:
        form = UserForm()
    response = render(request, "form.html", {"form":form})
    return response

def reg_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=new_user.username, password=request.POST["password"])
            login(request, user)
            return redirect("index")
    else:
        form = UserForm()
    response = render(request, "form.html", {"form":form})
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