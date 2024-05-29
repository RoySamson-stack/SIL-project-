from django.test import TestCase
from rest_framework.test import  APITestCase
from .models import Customer, Order
from django.urls import reverse
from rest_framework import status 


# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name='Customer Test', code="Python")


    def customer_create_test(self):
        customer = Customer.objects.get(code="Python")
        self.assertEqual(customer.name, "Test customer")



class CustomerAPITest(APITestCase):
    def setUp(self):
        self.customer_data = {'name': 'Test Customer', 'code': '1234'}
    
    def test_create_customer(self):
        response = self.client.post(reverse('customer-list'), self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class OrderModelTest(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Test Customer", code="TC123")
        Order.objects.create(customer=customer, item="Test Item", amount=100.00)

    def order_create_test(self):
        order = Order.objects.get(item="Test Item")
        self.assertEqual(order.amount, 100.00)



class OrderAPITest(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer', code='1234')
        self.order_data = {'customer': self.customer.id, 'item': 'Test Item', 'amount': '100.00'}
    
    # def test_create_order(self):
    #     response = self.client.post(reverse('order'), self.order_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_get_orders(self):
    #     response = self.client.get(reverse('order'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)