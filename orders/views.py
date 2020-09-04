from django.shortcuts import render, redirect
from .models import Order
from cart.models import Cart
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def make_order(request):
    email = request.POST.get('email')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    cart_id = request.session.get('cart_id', None)
    cart = Cart.objects.get(id=cart_id)
    if request.user.is_authenticated:
        order_obj = Order.objects.create(address=address, phone=phone, cart_id=cart_id)

        cart = Cart.objects.create(user=None)
        request.session['cart_id'] = cart.id
        request.session['cart_total'] = cart.products.count()
        cart.save()
    else:
        order_obj = Order.objects.create(email=email, address=address, phone=phone, cart_id=cart_id)
        cart = Cart.objects.create(user=None)
        request.session['cart_id'] = cart.id
        request.session['cart_total'] = cart.products.count()
        cart.save()

    context = {'order': order_obj}
    return render(request, 'orders/success.html', context)


