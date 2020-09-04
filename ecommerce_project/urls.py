
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import contact_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('contact/', contact_page),
    path('', include('products.urls', namespace='products')),
    path('', include('search.urls', namespace='search')),
    path('', include('cart.urls', namespace='cart')),
    path('', include('orders.urls', namespace='orders')),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
