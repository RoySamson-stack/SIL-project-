from django.urls import path, include
from .views import customer_page, create_order

urlpatterns = [
    path('accounts/', include('allauth.urls')), 
    path('customer/', customer_page, name='customer'),
    path('orders/create/', create_order, name='order-create'),
]
