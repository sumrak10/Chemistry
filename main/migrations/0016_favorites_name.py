# Generated by Django 4.2.2 on 2023-06-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_favoriteproduct_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorites',
            name='name',
            field=models.CharField(default='Избранное', max_length=24),
        ),
    ]