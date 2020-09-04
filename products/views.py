from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from cart.models import Cart




class ProductListView(ListView):
    queryset = Product.objects.all().active()
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'



class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.get_or_new(self.request)
        context['cart'] = cart_obj
        return context


