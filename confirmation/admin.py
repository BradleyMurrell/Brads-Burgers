from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    list_display = ('order_number', 'date', 'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
