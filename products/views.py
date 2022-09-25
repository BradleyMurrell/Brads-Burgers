from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Burger, Side, Drink
from .forms import BurgerForm, SideForm, DrinkForm


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


def add_burger(request):
    submitted = False
    if request.method == 'POST':
        form = BurgerForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_burger?submitted=True')
    else:
        form = BurgerForm
        if 'submitted' in request.GET:
            submitted = True
        ctx = {'form': form, 'submitted': submitted}
        return render(request, 'products/add_burger.html', ctx)


def add_side(request):
    submitted = False
    if request.method == 'POST':
        form = SideForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_side?submitted=True')
    else:
        form = SideForm
        if 'submitted' in request.GET:
            submitted = True
        ctx = {'form': form, 'submitted': submitted}
        return render(request, 'products/add_side.html', ctx)


def add_drink(request):
    submitted = False
    if request.method == 'POST':
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_drink?submitted=True')
    else:
        form = DrinkForm
        if 'submitted' in request.GET:
            submitted = True
        ctx = {'form': form, 'submitted': submitted}
        return render(request, 'products/add_drink.html', ctx)
