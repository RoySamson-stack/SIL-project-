from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, Customer
from .forms import OrderForm
import uuid
import africastalking


# username = 'sandbox'
# api_key = '33f28a48bbde171841669871ee5ff1e0f447099f885e161f7e0910ffc1f44205'
username = 'SilInterview'
api_key = '64709e0a8be635aeda4e1b98742ed8530f101ac2d1ab087aeb8d0a44e46505d0'

africastalking.initialize(username, api_key)
sms = africastalking.SMS


def login(request):
    return render(request, 'login.html')


@login_required
def customer_page(request):
    user = request.user
    if not hasattr(user, 'customer'):
        customer = Customer.objects.create(user=user, name=user.username, code=str(uuid.uuid4()))
    else:
        customer = user.customer


    orders = Order.objects.filter(customer=customer) 
    return render(request, 'SilInterview/customer.html',{'orders':orders})       

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
