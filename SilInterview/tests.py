from django.test import TestCase
from rest_framework.test import  APITestCase
from .models import Customer, Order
from django.urls import reverse
from rest_framework import status 
from django.contrib.auth.models import User 


# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test user", password="password-test")
        self.client.login(username="tst user", password="password-test")

        self.customer_data = {'name': 'test user', 'code': '1234'}


    def customer_create_test(self):
        response = self.client.post(reverse('customer'), self.customer_data, format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def get_oidc_token(self):
        return "your token "    



class OrderAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test user ', password='password-test')
        self.client.login(username='testuser', password='testpassword')
        

        self.customer = Customer.objects.create(name="Test customer", password="password-test")
        self.order_data = {'customer': self.customer.name, 'product': 'Test Product'}

    def test_create_order(self):
        response = self.client.post(reverse('order-create'), self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)