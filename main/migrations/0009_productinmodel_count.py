# Generated by Django 4.2.2 on 2023-06-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_basket_productinmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinmodel',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
