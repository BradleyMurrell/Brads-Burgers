from django.shortcuts import render

def orders(request):
    """A view to return the orders page"""

    return render(request, 'orders/orders.html')
