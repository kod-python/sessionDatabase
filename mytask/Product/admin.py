from django.contrib import admin

from .models import Product
# from .models import Order, OrderItem, Carts

from .models import CartItem,Carts, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)

admin.site.register(CartItem)
admin.site.register(Carts)

# admin.site.register(OrderItem)
# admin.site.register(Carts)
