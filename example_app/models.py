from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    data = models.DateField(default=django.utils.timezone.now)
    price = models.IntegerField()
    amount = models.IntegerField()


class Deal(models.Model):
    data = models.DateField(default=django.utils.timezone.now, verbose_name='Дата')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    amount = models.IntegerField(verbose_name='Количество')
    price_by_one = models.IntegerField(verbose_name='Цена за ед.')
    employer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return str(self.product) + " " + str(self.price_by_one)