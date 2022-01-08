from django.shortcuts import render
from .models import *


def storehome(request):
    products = Product.objects.all()
    context= {'products':products}
    return render(request, 'storefront/home.html', context)

def cart(request):
    context= {}
    return render(request, 'storefront/cart.html', context)

def checkout(request):
    context= {}
    return render(request, 'storefront/checkout.html', context)