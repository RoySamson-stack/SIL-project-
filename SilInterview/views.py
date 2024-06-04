import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, Customer
from .forms import OrderForm
import uuid
from django.views import View
import africastalking

username = 'SilInterview' 
api_key = '08f5b18ca6898e6996d87b0ccfdc407b8745dc5c0987db03d09060dac228aa62'  

try:
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
except Exception as e:
    print(f"Error initializing Africa's Talking: {e}")

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.customer
            order.save()

            phone_number = order.phonenumber
            message = f"Order Created: {order.item} for amount {order.amount}."
            try:
                response = sms.send(message, [phone_number])
                print(f"SMS sent successfully: {response}")
            except Exception as e:
                print(f"Error sending SMS: {e}")

            return redirect('customer')
    else:
        form = OrderForm()
    return render(request, 'SilInterview/order.html', {'form': form})
