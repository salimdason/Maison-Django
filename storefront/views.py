from django.shortcuts import render

def storehome(request):
    return render(request, 'storefront/home.html')

