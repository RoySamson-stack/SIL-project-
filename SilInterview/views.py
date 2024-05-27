from django.shortcuts import render

# Create your views here.
class CustomerView(view.ModelView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission = [isAuthenticated]


class OrderView(view.ModelView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission = [isAuthenticated]