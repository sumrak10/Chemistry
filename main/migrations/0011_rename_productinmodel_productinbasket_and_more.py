# Generated by Django 4.2.2 on 2023-06-10 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_product_stock_balance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductInModel',
            new_name='ProductInBasket',
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_balance',
            field=models.IntegerField(default=0, verbose_name='Остаток на складе'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]