from django.urls import path, include
from rest_framework.routers import Router
from .views import CustomerView, OrderView


router = Router()
router.register(r'customers', CustomerView)
router.register(r'orders', OrderView)

urlpatterns = [
    path('', include(router.urls))
]
