from django.shortcuts import render
from django.http import HttpResponse
from .models import Burger, Side, Drink
from .forms import ProductForm

def burgers(request):
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'products/burgers.html', ctx)

def sides(request):
    sides = Side.objects.all()
    ctx = {'sides': sides}
    return render(request, 'products/sides.html', ctx)

def drinks(request):
    drinks = Drink.objects.all()
    ctx = {'drinks': drinks}
    return render(request, 'products/drinks.html', ctx)


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
