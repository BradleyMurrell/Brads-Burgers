from django.shortcuts import render

def dashboard(request):
    """A view to return the dashboard page"""

    return render(request, 'dashboard/dashboard.html')
