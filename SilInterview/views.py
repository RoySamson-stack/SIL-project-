from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, Customer
from .forms import OrderForm



def login(request):
    return render(request, 'login.html')


@login_required
def customer_page(request):
    user = request.user
    if not hasattr(user, 'customer'):
        customer = Customer.objects.create(user=user, name=user.username, code="1234")
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
            return redirect('customer')
    else:
        form = OrderForm()
    return render(request, 'SilInterview/order.html', {'form': form})
