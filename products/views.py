from django.shortcuts import render
from .models import Burger, Side

def burgers(request):
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'products/burgers.html', ctx)

def sides(request):
    sides = Side.objects.all()
    ctx = {'sides': sides}
    return render(request, 'products/sides.html', ctx)
