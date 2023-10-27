from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['surname', 'name', 'phone_number']

    surname = forms.CharField(max_length=255, label="your name")
    name = forms.CharField(max_length=255, label="your surname")
    phone_number = forms.CharField(max_length=255,label="your phone number")