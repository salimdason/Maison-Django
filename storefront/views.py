from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def storehome(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = {"get_cart_total":0, "get_cart_items":0}

    products = Product.objects.all()
    context= {'products':products, "order": order}
    return render(request, 'storefront/home.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total":0, "get_cart_items":0}

    context= {"items": items, "order":order}
    return render(request, 'storefront/cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total":0, "get_cart_items":0}

    context= {"items": items, "order":order}

    return render(request, 'storefront/checkout.html', context)

def products(request):
    context= {}
    return render(request, 'storefront/products.html', context)

def about(request):
    context= {}
    return render(request, 'storefront/about.html', context)

def contact(request):
    context= {}
    return render(request, 'storefront/contact.html', context)

def updateItem(request):
    return JsonResponse('Item was added', safe=False)