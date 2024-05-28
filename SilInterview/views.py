from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, CustomerSerializer



# Create your views here.
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission = [IsAuthenticated]


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission = [IsAuthenticated]


def customer(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    return render(request, 'customer.html', customers=customers, orders=orders)   


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            return redirect(reverse('customer'))
        else:
            form = OrderForm()
        return render(request, 'order.html', {'form': form  })      

