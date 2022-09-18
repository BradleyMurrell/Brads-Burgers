from django import forms
from .models import Burger


class ProductForm(forms.ModelForm):

    class Meta:
        model = Burger
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
