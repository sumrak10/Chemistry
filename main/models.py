from django.db import models
from django.contrib.auth.models import User


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

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Товар "+self.name
    
    class Meta():
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ['id']



class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductInModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)