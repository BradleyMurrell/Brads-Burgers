from django import forms
from .models import Burger, Side, Drink


class BurgerForm(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ('name', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'})
        }


class SideForm(forms.ModelForm):
    class Meta:
        model = Side
        fields = ('name', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'})
        }


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('name', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'})
        }
