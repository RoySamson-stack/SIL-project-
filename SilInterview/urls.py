from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerView, OrderView


router = DefaultRouter()
router.register(r'customers', CustomerView, basename='customer')
router.register(r'orders', OrderView, basename='orders')

urlpatterns = [
    path('', views.customer, name='customer'),
    path('orders/create', views.order, name='order-create'),
]
