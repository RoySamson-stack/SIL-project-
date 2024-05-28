from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Customer, Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, CustomerSerializer
from .forms import OrderForm
from django.urls import reverse

# Create your views here.
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


def customer(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    return render(request, 'SilInterview/customer.html', {'customers': customers, 'orders': orders})


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('customer'))
    else:
        form = OrderForm()
    return render(request, 'SilInterview/order.html', {'form': form})
