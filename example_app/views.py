from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def suppliers(request):
    companies = Company.objects.all()
    form = CompanyForm()
    return render(request, 'suppliers.html', {'companies': companies, 'form': form})


def warehouse(request):
    warehouses = Warehouse.objects.all()
    form = WarehouseForm()
    return render(request, 'warehouse.html', {'warehouses': warehouses, 'form': form})


def products(request):
    productse = Product.objects.all()
    form = ProductForm()
    return render(request, 'products.html', {'productse': productse, 'form': form})


def create_product(request):
    if request.method == 'POST':
        formset = ProductForm(request.POST)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect("/products")


def create_company(request):
    if request.method == 'POST':
        formset = CompanyForm(request.POST)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect("/suppliers")


def create_warehouse(request):
    if request.method == 'POST':
        formset = WarehouseForm(request.POST)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect("/warehouse")


def deal(requset):
    deals = Deal.objects.all()
    return render(requset, 'deal.html', {'deals': deals})


def profile(request):
