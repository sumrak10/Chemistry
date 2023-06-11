from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import Category, Product, Basket, ProductInBasket, Order, ProductInOrder, Favorites, FavoriteProduct
from .forms import UserLoginForm, UserRegForm, ChangeUserForm, QuestionForm


def arender(request, template, context):
    try:
        current_user = User.objects.get(id=request.user.id)
    except:
        current_user = False
    context.update({"current_user": current_user})
    return render(request, template, context)

def index(request):
    categories = Category.objects.all()

    response = arender(request, "index.html", {"categories": categories})
    return response

def orders(request):
    orders = []
    orders_list = Order.objects.filter(user=request.user.id)
    for order in orders_list:
        products = ProductInOrder.objects.filter(order=order)
        orders.append({"order":order, "products":products})
    response = arender(request, "orders.html", {"orders":orders})
    return response

def about(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            response = arender(request, "status.html", {"status_text":"Ваш вопрос принят в обработку. Скоро с вами свяжется менеджер"})
            return response
    else:
        form = QuestionForm()
        
    response = arender(request, "about.html", {"form": form})
    return response


def category(request, id:int):
    category = Category.objects.get(id=id)
    products_list = Product.objects.filter(category=category)
    products_paginator = Paginator(products_list, 8) 

    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    products = products_paginator.get_page(page_number)
    response = arender(request, "category.html", {"category":category, "products": products,"mainpage":"search", "itssearch":False})
    return response


def product(request, id:int):
    product = Product.objects.get(id=id)
    # category = Category.objects.get(id=product.category.id)
    response = arender(request, "product.html", {"product": product})
    return response

def basket(request):
    context = {}
    if request.user.id is not None:
        basket = Basket.objects.get(user=request.user.id)
        products_in_basket = ProductInBasket.objects.filter(basket=basket)
        context.update({"products_in_basket":products_in_basket})
        context.update({"basket_summ":basket.summ})
    response = arender(request, "basket.html", context)
    return response

def favorites(request):
    if request.user.id is not None:
        favorites = Favorites.objects.get(user=request.user.id)
        fproducts = FavoriteProduct.objects.filter(favorites=favorites)
        products_list = []
        for fproduct in fproducts:
            products_list.append(fproduct.product)
        products_paginator = Paginator(products_list, 4) 

        page_number = request.GET.get('page')
        if page_number is None:
            page_number = 1
        products = products_paginator.get_page(page_number)
        response = arender(request, "favorites.html", {"category":favorites, "products": products})
        return response
    
def search(request):
    query = request.GET.get('query')
    if not query:
        return redirect(request.META.get('HTTP_REFERER'))
    products_list = Product.objects.filter(name__contains=query.lower()) | Product.objects.filter(des__contains=query.lower()) |       Product.objects.filter(name__contains=query.upper()) | Product.objects.filter(des__contains=query.upper()) |       Product.objects.filter(name__contains=query.capitalize()) | Product.objects.filter(des__contains=query.capitalize())        
    
    products_paginator = Paginator(products_list, 8) 

    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    products = products_paginator.get_page(page_number)

    founded = True
    if not products_list.count():
        founded = False
    
    class Meta:
        name = "Поиск"

    return arender(request, 'search.html', {"category":Meta,"products":products, "founded":founded, "query":query, "mainpage":"search", "itssearch":True})


def create_order(request):
    if request.user.id is not None:
        basket = Basket.objects.get(id=request.user.id)
        products_in_basket = ProductInBasket.objects.filter(basket=basket)
        order = Order()
        user = User.objects.get(id=request.user.id)
        order.user = user
        order.summ = basket.summ
        order.save()
        for product_in_basket in products_in_basket:
            product_in_order = ProductInOrder()
            product_in_order.product = product_in_basket.product
            product_in_order.count = product_in_basket.count
            product_in_order.order = order
            product_in_order.save()
            product_in_basket.delete()
        basket.save()
        response = arender(request, "status.html", {"status_text":"Ваш заказ принят в обработку"})
        return response


def change_user_data(request):
    if request.method == 'POST':
        if request.user.id is None:
            return redirect("login")
        user = User.objects.get(id=request.user.id)
        form = ChangeUserForm(request.POST, instance=user)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect("index")
    else:
        if request.user.id is None:
            return redirect("login")
        user = User.objects.get(id=request.user.id)
        form = ChangeUserForm(instance=user)
    response = arender(request, "form.html", {"form":form, "action": "/change_user/"})
    return response

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("index")
        form = UserLoginForm(request.POST)
    else:
        form = UserLoginForm()
    response = arender(request, "form.html", {"form":form, "action": "/login/"})
    return response

def reg_view(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=new_user.username, password=request.POST["password"])
            login(request, user)
            basket = Basket()
            basket.user = user
            basket.save()
            fav = Favorites()
            fav.user = user
            fav.save()
            return redirect("index")
    else:
        form = UserRegForm()
    response = arender(request, "form.html", {"form":form, "action": "/reg/"})
    return response

def logout_view(request):
    logout(request)
    return redirect("index")

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        if request.user.id is not None:
            product_id = request.POST["product_id"]
            count = request.POST["count"]
            product = Product.objects.get(id=product_id)
            basket = Basket.objects.get(user=request.user.id)
            pib = ProductInBasket()
            pib.product = product
            pib.count = count
            pib.basket = basket
            pib.save()
            basket.save()
            return JsonResponse({"message":"added", "summ":basket.summ})
@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        if request.user.id is not None:
            product_id = request.POST["product_id"]
            count = request.POST["count"]
            product = ProductInBasket.objects.get(id=product_id)
            product.count = count
            product.save()
            basket = Basket.objects.get(user=request.user.id)
            basket.save()
            return JsonResponse({"message":"updated", "summ":basket.summ})
@csrf_exempt
def delete_product(request):
    if request.method == 'POST':
        if request.user.id is not None:
            product_id = request.POST["product_id"]
            count = request.POST["count"]
            product = ProductInBasket.objects.get(id=product_id)
            product.delete()
            basket = Basket.objects.get(user=request.user.id)
            basket.save()
            return JsonResponse({"message":"updated", "summ":basket.summ})
@csrf_exempt 
def in_favorites(request):
    if request.method == 'POST':
        if request.user.id is not None:
            product_id = request.POST["product_id"]
            favorites = Favorites.objects.get(user=request.user.id)
            product = Product.objects.get(id=product_id)
            try:
                favorite_product = FavoriteProduct.objects.get(product=product)
                favorite_product.delete()
                return JsonResponse({"message":"deleted"})
            except:
                favorite_product = FavoriteProduct()
                favorite_product.product = product
                favorite_product.favorites = favorites
                favorite_product.save()
                return JsonResponse({"message":"added"})