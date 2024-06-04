from django import forms
from .models import Order
from django.views import View
from django.core.exceptions import ValidationError



def validate_phone_number(value):
    if not value.startswith('+254'):
        raise ValidationError('Phone number must start with country code +254.')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'amount', 'phonenumber']


    phonenumber = forms.CharField(required=True, 
    widget=forms.TextInput(attrs={
            'placeholder': 'e.g., +254702683107'
        })
    )    

