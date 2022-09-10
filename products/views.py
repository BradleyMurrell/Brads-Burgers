from django.shortcuts import render

def products(request):
    """A view to return the products page"""

    return render(request, 'products.html')
