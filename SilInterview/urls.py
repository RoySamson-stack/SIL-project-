from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerView, OrderView
from . import views 


router = DefaultRouter()
router.register(r'customers', CustomerView, basename='customer')
router.register(r'orders', OrderView, basename='orders')

urlpatterns = [
    path('', views.Customer, name='customer'),
    path('orders/create', views.Order, name='order-create'),
    path('', include(router.urls))
]
