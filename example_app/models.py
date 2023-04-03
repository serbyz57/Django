from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)