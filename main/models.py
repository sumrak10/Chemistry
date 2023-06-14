from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


class Question(models.Model):
    fio = models.CharField(max_length=128, verbose_name="Имя Фамилия")
    contacts = models.CharField(max_length=128, verbose_name="Контакты")
    text = models.TextField(verbose_name="Текст обращения")

    def __str__(self):
        return "Обращение от " + self.fio
    
    class Meta():
        verbose_name = "обращение"
        verbose_name_plural = "Обращения"
        ordering = ['id']

class Category(models.Model):

    name = models.CharField(max_length=128, verbose_name="Наименование")
    des = models.TextField(verbose_name="Описание", default="")
    img = models.ImageField(upload_to='products/',default='products/placeholder.png', verbose_name="Фотография")

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "категория"
        verbose_name_plural = "Категории"
        ordering = ['id']



class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name="Наименование")
    des = models.TextField(verbose_name="Описание", default="")
    price = models.IntegerField(verbose_name="Цена")
    img = models.ImageField(upload_to='products/',default='products/placeholder.png', verbose_name="Фотография")
    stock_balance = models.IntegerField(default=0, verbose_name="Остаток на складе")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Товар "+self.name
    
    class Meta():
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ['id']



class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=24, default="Избранное")

    def __str__(self):
        return "Избранное пользователя  " + self.user.username
    
    class Meta():
        verbose_name = "избранное"
        verbose_name_plural = "Избранное"
        ordering = ['id']

class FavoriteProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE)

    def __str__(self):
        return "Избранное пользователя"
    
    class Meta():
        verbose_name = "избранное"
        verbose_name_plural = "Избранное"
        ordering = ['id']

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summ = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        products = ProductInBasket.objects.filter(basket=self)
        summ = 0
        for product in products:
            summ += product.product.price * product.count
        self.summ = summ
        super().save(*args, **kwargs)

    def __str__(self):
        return "Корзина пользователя  " + self.user.username
    
    class Meta():
        verbose_name = "корзина"
        verbose_name_plural = "Корзины"
        ordering = ['id']

class Order(models.Model):
    class Status(models.IntegerChoices):
        new = 1, _("Новый")
        procces = 2, _("В обработке")
        closed = 3, _("Закрыт")
        succesfull = 4, _("Завершен")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Клиент")
    summ = models.IntegerField(default=0, verbose_name="Сумма")
    status = models.IntegerField(choices=Status.choices, default=Status.new, verbose_name="Статус")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return "Заказ от пользователя  " + self.user.username
    
    class Meta():
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"
        ordering = ['id']

class ProductInBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.IntegerField()
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

    def __str__(self):
        return  "Продукт"
    
    class Meta():
        verbose_name = "продукт в корзине"
        verbose_name_plural = "Продукты в корзине"
        ordering = ['id']

class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return  "Продукт"
    
    class Meta():
        verbose_name = "продукт в заказе"
        verbose_name_plural = "Продукты в заказе"
        ordering = ['id']


class ChangePasswordUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    secret = models.CharField(max_length=24, default="Секретный код")