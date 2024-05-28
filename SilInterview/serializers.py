from rest_framework import serializers
from .models import Customer , Order 



class CustomerSerializer(serializers.Serializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code']

    def create(self,validated):
        return Customer.object.create(validated=validated)   


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'time']
        