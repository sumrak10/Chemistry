from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import Category, Product, Basket, ProductInModel
from .forms import UserLoginForm, UserRegForm


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

def category(request, id:int):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    response = arender(request, "category.html", {"category":category, "products": products})
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
        product_id = request.POST["product_id"]
        count = request.POST["count"]
        product = Product.objects.get(id=product_id)
        basket = Basket.objects.get(id=user_id)
        pib = ProductInModel()
        pib.product = product
        pib.basket
        return JsonResponse({"message":"added"})