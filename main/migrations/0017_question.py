# Generated by Django 4.2.2 on 2023-06-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_favorites_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=128, verbose_name='Имя Фамилия')),
                ('contacts', models.CharField(max_length=128, verbose_name='Контакты')),
                ('text', models.TextField(verbose_name='Текст обращения')),
            ],
        ),
    ]