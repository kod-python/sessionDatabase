from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .cart import Cart
from .models import Product
from django.contrib import messages
# from .models import  Order, OrderItem, Cart

from .models import Order,CartItem,Carts
from .forms import CheckoutForm




def index(request):
 
    products = Product.objects.all()
    cart = Cart(request)
    
    product_count = cart.get_product_count()
 
    return render(request, 'index.html', {'products': products, 'product_count':product_count})




def checkout_success(request):
    
    return render(request , 'checkout_success.html')

def cart_font(request):
    
    return render(request, 'cart_font.html')



def display(request):
    
    return render(request, 'display.html')





def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})



# def order_confirmation(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request, 'order_confirmation.html', {'order': order})










def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            shipping_address = form.cleaned_data['shipping_address']
            billing_address = form.cleaned_data['billing_address']
            payment_method = form.cleaned_data['payment_method']

            # Ensure cart_items is a list or queryset of cart items
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)

            if not cart_items.exists():
                return render(request, 'checkout.html', {'form': form, 'error': 'Your cart is empty.'})

            # Calculate the total price
            total_price = sum(item.product.price * item.quantity for item in cart_items)

            # Create the order
            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                shipping_address=shipping_address,
                billing_address=billing_address,
                payment_method=payment_method
            )

            # Optionally, clear the cart items after creating the order
            cart_items.delete()

            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form})



# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             shipping_address = form.cleaned_data['shipping_address']
#             billing_address = form.cleaned_data['billing_address']
#             payment_method = form.cleaned_data['payment_method']

#             # Ensure cart_items is a list or queryset of cart items
#             cart = get_object_or_404(Carts, user=request.user)
#             cart_items = CartItem.objects.filter(cart=cart)

#             # Calculate the total price
#             total_price = sum(item.product.price * item.quantity for item in cart_items)

#             # Create the order
#             order = Order.objects.create(
#                 user=request.user,
#                 total_price=total_price,
#                 shipping_address=shipping_address,
#                 billing_address=billing_address,
#                 payment_method=payment_method
#             )

#             # Optionally, clear the cart items after creating the order
#             cart_items.delete()

#             return redirect('order_confirmation', order_id=order.id)
#     else:
#         form = CheckoutForm()

#     return render(request, 'checkout.html', {'form': form})











# def checkout(request):
#     cart_items = Carts(request)
#     if not cart_items:
#         return redirect('cart_detail')  

#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             shipping_address = form.cleaned_data['shipping_address']
#             billing_address = form.cleaned_data['billing_address']
#             payment_method = form.cleaned_data['payment_method']
          
#             total_price = sum(item.product.price * item.quantity for item in cart_items)
#             order = Order.objects.create(
#                 user=request.user,
#                 total_price=total_price,
#                 shipping_address=shipping_address,
#                 billing_address=billing_address,
#                 payment_method=payment_method
#             )

#             for item in cart_items:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item.product,
#                     quantity=item.quantity,
#                     price=item.product.price
#                 )

#             cart_items.delete() 

#             return redirect( 'checkout_success', order=order)
#     else:
#         form = CheckoutForm()

#     return render(request, 'checkout.html', {'form': form, 'cart_items': cart_items})











def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.add(product, quantity)
        return redirect('cart_detail')
    return render(request, 'product_detail.html', {'product': product})




def cart_detail(request):
    cart = Cart(request)
    item_count = cart.get_item_count()
    return render(request, 'cart_detail.html', {'cart': cart, 'item_count':item_count})

    


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = int(request.POST.get('quantity', 1))
    
    cart = Cart(request)
    cart.add(product_id=product.id, quantity=quantity)
    
    messages.success(request, "Product added to cart successfully")
    return redirect('display')




def update_cart(request, product_id):
    cart = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get('quantity'))
    cart.update_quantity(product_id, quantity)
    messages.success(request, "Cart updated successfully")
    return redirect('cart_detail')    
    



def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    messages.success(request, "Product removed from cart successfully")
    return redirect('cart_detail')




def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, "Cart cleared successfully")
    return redirect('cart_detail')



