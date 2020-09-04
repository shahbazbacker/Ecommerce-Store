from django.db import models
from products.models import Product
from django.conf import settings
from django.db.models.signals import m2m_changed

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def get_or_new(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            print('cart exists')
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            print('cart created')
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=0, default=200)
    # quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def cart_save(sender, instance, action, *args, **kwargs):
    print(action)
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
    	products = instance.products.all()
    	total_price = 0
    	for product in products:
     		total_price += product.price
    	instance.total = total_price
    	instance.save()

m2m_changed.connect(cart_save, sender=Cart.products.through)



