from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from .forms import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def suppliers(request):
    company1, created = Company.objects.get_or_create(name="Диллер")
    company2, created = Company.objects.get_or_create(name='Китай')
    companies = Company.objects.all()
    return render(request, 'suppliers.html', {'company1': company1, 'company2': company2, 'companies': companies})


def warehouse(request):
    return render(request, 'warehouse.html')


def products(request):
    productse = Product.objects.all()
    companies = Company.objects.all()
    form = ProductForm()
    return render(request, 'products.html', {'productse': productse, 'companies': companies, 'form': form})


def create(request):
    if request.method == 'POST':
        formset = ProductForm(request.POST)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect("/products")
