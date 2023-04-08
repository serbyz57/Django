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
    path('create/', create),
]
urlpatterns += staticfiles_urlpatterns()