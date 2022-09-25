from django.db import models


class Order(models.Model):
    number = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, null=True)
