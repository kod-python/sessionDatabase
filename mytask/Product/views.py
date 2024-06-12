from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .cart import Cart
from .models import Product
from django.contrib import messages
from .models import  Order, OrderItem, Carts

# from .models import Order,CartItem,Carts
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
    cart = Cart(request)
    
    return render(request, 'order_confirmation.html', {'order': order, 'cart':cart})






def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            company_name = form.cleaned_data['company_name']
            address = form.cleaned_data['address']
            house_number_street_name = form.cleaned_data['house_number_street_name']
            town_city = form.cleaned_data['town_city']
            country = form.cleaned_data['country']
            postcode_zip = form.cleaned_data['postcode_zip']
            mobile = form.cleaned_data['mobile']
            email_address = form.cleaned_data['email_address']
            create_account = form.cleaned_data['create_account']
            ship_to_different_address = form.cleaned_data['ship_to_different_address']
            payment_method = form.cleaned_data['payment_method']

            cart = get_object_or_404(Carts, user=request.user)
            cart_items = OrderItem.objects.filter(cart=cart)

          
            total_price = 0
            for item in cart_items:
                item.sub_total = item.product.price * item.quantity
                total_price += item.sub_total

          
            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                address=address,
                house_number_street_name=house_number_street_name,
                town_city=town_city,
                country=country,
                postcode_zip=postcode_zip,
                mobile=mobile,
                email_address=email_address,
                total_price=total_price,
                payment_method=','.join(payment_method)  
            )

          
            if ship_to_different_address:
              
                pass

          
            cart_items.delete()

            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()
    

    cart = get_object_or_404(Carts, user=request.user)
    cart_items = OrderItem.objects.filter(cart=cart)
    
   
    for item in cart_items:
        item.sub_total = item.product.price * item.quantity

    return render(request, 'checkout.html', {'form': form, 'cart':cart})























# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             company_name = form.cleaned_data['company_name']
#             address = form.cleaned_data['address']
#             house_number_street_name = form.cleaned_data['house_number_street_name']
#             town_city = form.cleaned_data['town_city']
#             country = form.cleaned_data['country']
#             postcode_zip = form.cleaned_data['postcode_zip']
#             mobile = form.cleaned_data['mobile']
#             email_address = form.cleaned_data['email_address']
#             create_account = form.cleaned_data['create_account']
#             ship_to_different_address = form.cleaned_data['ship_to_different_address']
#             payment_method = form.cleaned_data['payment_method']

#             # Retrieve the cart and cart items
#             cart = get_object_or_404(Carts, user=request.user)
#             cart_items = OrderItem.objects.filter(cart=cart)

           
#             total_price = 0
#             for item in cart_items:
#                 item.sub_total = item.product.price * item.quantity
#                 total_price += item.sub_total

#             order = Order.objects.create(
#                 user=request.user,
#                 first_name=first_name,
#                 last_name=last_name,
#                 company_name=company_name,
#                 address=address,
#                 house_number_street_name=house_number_street_name,
#                 town_city=town_city,
#                 country=country,
#                 postcode_zip=postcode_zip,
#                 mobile=mobile,
#                 email_address=email_address,
#                 total_price=total_price,
#                 payment_method=','.join(payment_method)  
#             )

            
#             if ship_to_different_address:
               
#                 pass

           
#             cart_items.delete()

#             return redirect('order_confirmation', order_id=order.id)
#     else:
#         form = CheckoutForm()
#         cart = get_object_or_404(Carts, user=request.user)
#         cart_items = OrderItem.objects.filter(cart=cart)
        
       
#         for item in cart_items:
#             item.sub_total = item.product.price * item.quantity

#     return render(request, 'checkout.html', {'form': form, cart_items, 'total_price':total_price})



















# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             company_name = form.cleaned_data['company_name']
#             address = form.cleaned_data['address']
#             house_number_street_name = form.cleaned_data['house_number_street_name']
#             town_city = form.cleaned_data['town_city']
#             country = form.cleaned_data['country']
#             postcode_zip = form.cleaned_data['postcode_zip']
#             mobile = form.cleaned_data['mobile']
#             email_address = form.cleaned_data['email_address']
#             create_account = form.cleaned_data['create_account']
#             ship_to_different_address = form.cleaned_data['ship_to_different_address']
#             payment_method = form.cleaned_data['payment_method']

#             # Here you can handle the `create_account` logic if needed
#             # For example, creating a new user account

#             # Retrieve the cart and cart items
#             cart = get_object_or_404(Carts, user=request.user)
#             cart_items = OrderItem.objects.filter(cart=cart)

#             # Calculate the total price of the cart
#             total_price = sum(item.product.price * item.quantity for item in cart_items)

#             # Create an order
#             order = Order.objects.create(
#                 user=request.user,
#                 first_name=first_name,
#                 last_name=last_name,
#                 company_name=company_name,
#                 address=address,
#                 house_number_street_name=house_number_street_name,
#                 town_city=town_city,
#                 country=country,
#                 postcode_zip=postcode_zip,
#                 mobile=mobile,
#                 create_account=create_account,
#                 email_address=email_address,
#                 total_price=total_price,
#                 payment_method=','.join(payment_method)  # Store selected payment methods as a comma-separated string
#             )

#             # If shipping to a different address, handle that logic here
#             if ship_to_different_address:
#                 # Add logic for handling different shipping address if needed
#                 pass

#             # Clear the cart items
#             cart_items.delete()

#             return redirect('order_confirmation', order_id=order.id)
#     else:
#         form = CheckoutForm()

#     return render(request, 'checkout.html', {'form': form})


















# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             mobile = form.cleaned_data['mobile']
#             shipping = form.cleaned_data['shipping']

#             cart = get_object_or_404(Carts, user=request.user)
#             cart_items = OrderItem.objects.filter(cart=cart)

        
#             total_price = sum(item.product.price * item.quantity for item in cart_items)

#             order = Order.objects.create(
#                 user=request.user,
#                 total_price=total_price,
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 mobile=mobile,
#                 shipping=shipping
#             )

         
#             cart_items.delete()

#             return redirect('order_confirmation', order_id=order.id)
#     else:
#         form = CheckoutForm()

#     return render(request, 'checkout.html', {'form': form})








# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             shipping_address = form.cleaned_data['shipping_address']
#             billing_address = form.cleaned_data['billing_address']
#             payment_method = form.cleaned_data['payment_method']

          
#             cart = get_object_or_404(Carts, user=request.user)
#             cart_items = OrderItem.objects.filter(cart=cart)

        
#             total_price = sum(item.product.price * item.quantity for item in cart_items)

#             order = Order.objects.create(
#                 user=request.user,
#                 total_price=total_price,
#                 shipping_address=shipping_address,
#                 billing_address=billing_address,
#                 payment_method=payment_method
#             )

         
#             cart_items.delete()

#             return redirect('order_confirmation', order_id=order.id)
#     else:
#         form = CheckoutForm()

#     return render(request, 'checkout.html', {'form': form})



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



