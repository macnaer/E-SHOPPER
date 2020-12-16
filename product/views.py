from django.shortcuts import render
from django.shortcuts import get_object_or_404
from product.models import Product
from .cart import Cart
from django.conf import settings


def cart(request, product_id):
    print("product_id ", product_id)
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    context = {
        "products": product,
    }
    cart = Cart(request)
    cart.add(product)
    return render(request, "pages/cart.html",context)