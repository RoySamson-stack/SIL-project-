from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'amount', 'phonenumber']


    phonenumber = forms.CharField(required=True, help_text="Enter phone number ")    

