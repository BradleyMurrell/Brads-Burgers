from django.shortcuts import render

def confirmation(request):
    """A view to return the confirmation page"""

    return render(request, 'confirmation/confirmation.html')
