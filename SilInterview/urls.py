from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerView, OrderView


router = DefaultRouter()
router.register(r'customers', CustomerView)
router.register(r'orders', OrderView)

urlpatterns = [
    path('', include(router.urls))
]
