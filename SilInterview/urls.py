from django.urls import path, include
from .views import customer_page, create_order,  CustomLogoutView
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('accounts/', include('allauth.urls')),
    path('customer/', customer_page, name='customer'),
    path('orders/create/', create_order, name='order-create'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]