from django import forms
from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product

        fields = ['name', 'description']
        labels = {
            'name': 'Наименование товара', 'description': 'Описание товара'
        }


class CompanyForm(ModelForm):
    class Meta:
        model = Company

        fields = ['name']
        labels = {'name': 'Название компании'}


class WarehouseForm(ModelForm):

    class Meta:
        model = Warehouse

        fields = ['product', 'company', 'data', 'price', 'amount']
        labels = {'product': 'Наименование товара', 'company': 'Название компании', 'data': 'Дата поставки',
                  'price': 'Цена', 'amount': 'Количество'}


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=11,
                            label='Логин',
                            widget=forms.TextInput(attrs={'type': 'text', 'class': "field"}))
    password = forms.CharField(max_length=15,
                               label='Пароль',
                               widget=forms.TextInput(attrs={'type': 'text', 'class': "field"}))
    email = forms.EmailField(label="Email",
                            widget=forms.TextInput(attrs={'type': 'email', 'class': "field"}))


class LoginForm(forms.Form):
    login = forms.CharField(max_length=11,
                            label='Логин',
                            widget=forms.TextInput(attrs={'type': 'text', 'class': "field"}))
    password = forms.CharField(max_length=15,
                               label='Пароль',
                               widget=forms.TextInput(attrs={'type': 'text', 'class': "field"}))
