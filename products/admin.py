from django.contrib import admin
from .models import Product, Contact


admin.site.register(Contact)
admin.site.register(Product)