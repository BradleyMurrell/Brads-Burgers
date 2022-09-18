from django.urls import path
from . import views

urlpatterns = [
    path('confirmation', views.confirmation, name='confirmation'),
    path('complete', views.complete, name='complete')
]
