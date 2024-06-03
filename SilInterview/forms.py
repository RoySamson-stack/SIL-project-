from django import forms
from .models import Order
from django.views import View

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'amount', 'phonenumber']


    phonenumber = forms.CharField(required=True, )    

