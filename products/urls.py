from django.urls import path
from . import views

urlpatterns = [
    path('burgers', views.burgers, name='burgers'),
    path('sides', views.sides, name='sides'),
    path('drinks', views.drinks, name='drinks'),
    path('add/', views.add_product, name='add_product'),
]
