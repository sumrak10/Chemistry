from django.db import models



class Category(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name="Наименование")
    price = models.IntegerField(verbose_name="Цена")
    img = models.ImageField(upload_to='products/',default='product/placeholder.png', verbose_name="Фотография")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Товар "+self.name
    
    # class Meta():
    #     verbose_name = "члена команды"
    #     verbose_name_plural = "Члены команды"
    #     ordering = ['name']
