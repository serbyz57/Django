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
    company, created = Company.objects.bulk_get_or_create[(name="Диллер"), (name="Китай")]
    return render(request, 'suppliers.html', {'company': company})


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
