from rest_framework import serializers
from .models import Customer , Order 



class CusomerSerializer(serializers.Serializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code']


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'time']
        