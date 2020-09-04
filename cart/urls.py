from django.urls import path
from .views import cartview, cart_update

app_name = 'cart'

urlpatterns = [
    path('cart/', cartview, name="cart_page"),
    path('cart_update/', cart_update, name="cart_update"),
    
]

