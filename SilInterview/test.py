from django.test import TestCase
from .models import Customer, Order


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name='Customer Test', code="Python")


    def customer_create_test(self):
        customer = Customer.objects.get(code="Python")
        self.assertEqual(customer.name, "Test customer")



class OrderModelTest(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Test Customer", code="TC123")
        Order.objects.create(customer=customer, item="Test Item", amount=100.00)

    def order_create_test(self):
        order = Order.objects.get(item="Test Item")
        self.assertEqual(order.amount, 100.00)