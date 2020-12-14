from decimal import Decimal
from django.conf import settings
from product.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = { "tittle" : str(product.tittle), "price" : str(product.price)}
        print(self.session['cart'])
        self.save()
        # print(self.cart)

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True