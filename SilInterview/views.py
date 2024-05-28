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