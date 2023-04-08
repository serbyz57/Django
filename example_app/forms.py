from django import forms
from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product

        fields = ['name', 'description', 'company']
        labels = {
            'name': 'Наименование товара', 'description': 'Описание товара', 'company': 'Поставщик'
        }


class CompanyForm(ModelForm):
    class Meta:
        model = Company

        fields = ['name']
        labels = {'name': 'Название компании'}
