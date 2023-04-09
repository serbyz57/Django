from django.db import models
import datetime


class Company(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)


class Warehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    data = models.DateField(default=datetime.date.today())
    price = models.IntegerField()
    amount = models.IntegerField()
