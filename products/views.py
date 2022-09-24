from django.shortcuts import render, redirect, reverse
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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_product'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
