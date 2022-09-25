from django.urls import path
from . import views

urlpatterns = [
    path('burgers', views.burgers, name='burgers'),
    path('sides', views.sides, name='sides'),
    path('drinks', views.drinks, name='drinks'),
    path('product_management', views.product_management, name='product_management'),
    path('add_burger', views.add_burger, name='add_burger'),
    path('add_side', views.add_side, name='add_side'),
    path('add_drink', views.add_drink, name='add_drink')
]
