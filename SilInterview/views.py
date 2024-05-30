from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm

@login_required
def customer_page(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=request.user.customer)
    return render(request, 'customer.html', {'orders': orders})

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
    return render(request, 'order.html', {'form': form})
