from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchView(ListView):
    template_name = 'search/search_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = self.request.GET.get('q', None)
        if qs is not None: 
            return Product.objects.filter(name__icontains=qs)
        return Product.objects.all()


