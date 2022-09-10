from django.shortcuts import render
from .models import Burger

def products(request):
    """A view to return the products page"""
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'products/products.html', ctx)
