from django.db import models
from cart.models import Cart
from django.db.models.signals import post_save

ORDER_CHOICES = (('created', 'Created'),
				('paid', 'Paid'),
				('shipped', 'Shipped'),
				('cancelled', 'cancelled'),
				('refund', 'Refund'),)

class Order(models.Model):
	address = models.CharField(max_length=255)
	phone = models.DecimalField(max_digits=10, decimal_places=0)
	email = models.EmailField(null=True, blank=True)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	status = models.CharField(max_length=255, default='created', choices=ORDER_CHOICES)


	def __str__(self):
		return str(self.id)

def cart_total(sender, instance, *args, **kwargs):
	cart_obj = instance
	cart_total = cart_obj.total
	cart_id = cart_obj.id
	qs = Order.objects.filter(cart__id=cart_id)
	if qs.count() ==1:
		order_obj = qs.first()
		order_obj.total = cart_total
		order_obj.save()

post_save.connect(cart_total, sender=Cart)