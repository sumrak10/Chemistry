"""
URL configuration for chemistry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('about/', views.about),
    path('category/<int:id>/', views.category),
    path('product/<int:id>/', views.product),
    path('basket/', views.basket),
    path('favorites/', views.favorites),
    path('search/', views.search, name='search'),
    path('create_order/', views.create_order),

    path('add_product/', views.add_product),
    path('update_product/', views.update_product),
    path('delete_product/', views.delete_product),
    path('in_favorites/', views.in_favorites),

    path('change_user/', views.change_user_data, name='change_user'),
    path('login/', views.login_view, name='login'),
    path('reg/', views.reg_view, name='reg'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

