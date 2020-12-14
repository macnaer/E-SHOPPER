from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Product
from .cart import Cart


def product(request, product_id):
    # product = get_object_or_404(Products, pk=product_id)
    # print(product)
    # context = {
    #     "product": product,

    # }
    # return render(request, "pages/cart.html", context)
    pass
# def cart2(request):
#     print("cart ", cart)
#     context = {

#     }
#     return render(request, "pages/cart.html", context)


def cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    context = {
        "products": product,
    }
    print(context)
    cart = Cart(request)
    print(cart)
    cart.add(product)
    return render(request, "pages/cart.html", {'cart': cart})


# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')
