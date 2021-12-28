from django.shortcuts import render

def storehome(request):
    return render(request, 'storefront/index.html')

# from django.template.loader import get_template
# from django.http import HttpResponse

# def home(request):
#     template = get_template('app1/home.html')
#     context = {

#     }
#     return HttpResponse(template.render(context, request))