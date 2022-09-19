from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def confirmation(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['order'] = request.POST.get('orders')
    return render(request, 'confirmation/confirmation.html')

def complete(request):

    return render(request, 'confirmation/complete.html')
