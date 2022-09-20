from django.db import models
from products.models import Burger, Side, Drink


class Order(models.Model):
    order_number = models.CharField(max_length=3, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    burger = models.ForeignKey(Burger, null=False, blank=False, on_delete=models.CASCADE)
    side = models.ForeignKey(Side, null=False, blank=False, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, null=False, blank=False, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
