from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def suppliers(request):
    return render(request, 'suppliers.html')

def warehouse(request):
    return render(request, 'warehouse.html')

def products(request):
    return render(request, 'products.html')