from django.contrib import admin
from .models import Burger, Side

class BurgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Burger, BurgerAdmin)


class SideAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Side, SideAdmin)
