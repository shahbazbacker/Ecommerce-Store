from django.shortcuts import render, redirect
from cart.models import Cart
from products.models import Product


def new_cart(user=None):
    user_obj = None
    if user is not None:
        if user.is_authenticated:
            user_obj = user
    return Cart.objects.create(user=user_obj)



def cartview(request):
    # cart_obj = Cart.objects.get_or_new(request)
    cart_id = request.session.get("cart_id", None)
    cart_obj = Cart.objects.get(id=cart_id)
    print(cart_obj)
    context = {'cart':cart_obj}
    return render(request, 'cart/cart_page.html', context)


def cart_update(request):

    pdt_id = request.POST.get('product')
    print(pdt_id)
    obj = Product.objects.get(id=pdt_id)
    cart_obj, new_obj = Cart.objects.get_or_new(request)
    if obj in cart_obj.products.all():
        cart_obj.products.remove(obj)
    else:
        cart_obj.products.add(obj)
    request.session['cart_total'] = cart_obj.products.count()
    return redirect('cart:cart_page')


