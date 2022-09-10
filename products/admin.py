from django.contrib import admin
from .models import Burger, Side, Drink

class BurgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Burger, BurgerAdmin)


class SideAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Side, SideAdmin)

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Drink, DrinkAdmin)
