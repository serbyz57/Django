from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index),
    path('about', about),
    path('contact', contact),
    path('suppliers', suppliers),
    path('warehouse', warehouse),
    path('products', products),
    path('deal', deal),
    path('create_product/', create_product),
    path('create_company/', create_company),
    path('create_warehouse/', create_warehouse),
    path('profile', profile)
]
urlpatterns += staticfiles_urlpatterns()
