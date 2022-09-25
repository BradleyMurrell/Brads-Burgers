from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ('number', 'total', 'date',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
