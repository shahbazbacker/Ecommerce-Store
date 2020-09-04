from django.urls import path
from .views import make_order

app_name = 'orders'

urlpatterns = [
    path('order', make_order, name="cart_page"),
    
]

