from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, Customer
from .forms import OrderForm
import uuid
from django.views import View
import africastalking


# username = 'sandbox'
# api_key = '33f28a48bbde171841669871ee5ff1e0f447099f885e161f7e0910ffc1f44205'
username = 'SilInterview'
api_key = '08f5b18ca6898e6996d87b0ccfdc407b8745dc5c0987db03d09060dac228aa62'

africastalking.initialize(username, api_key)
sms = africastalking.SMS


# def login(request):
#     return render(request, 'login.html')


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


@login_required
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = OrderForm(instance=order)
    return render(request, 'SilInterview/order-update.html', {'form': form, 'order': order})

@login_required
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('customer')
    return render(request, 'SilInterview/order-delete.html', {'order': order})

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/accounts/login/')