from django.urls import path
from . import views

urlpatterns = [
    path('', views.storehome, name='store-home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
]