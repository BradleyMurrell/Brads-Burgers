from django.shortcuts import render
from .models import Burger

def burgers(request):
    """A view to return the burgers page"""
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'products/burgers.html', ctx)
