from django.shortcuts import render

def confirmation(request):
    """A view to return the confirmation page"""

    return render(request, 'confirmation/confirmation.html')

def complete(request):
    """A view to return the complete page"""

    return render(request, 'confirmation/complete.html')
