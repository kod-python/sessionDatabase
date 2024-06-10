from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .cart import Cart
from .models import Product
from django.contrib import messages




def index(request):
 
    products = Product.objects.all()
    cart = Cart(request)
    item_count = cart.get_item_count()
    return render(request, 'index.html', {'products': products, 'item_count':item_count})




def cart_font(request):
    
    return render(request, 'cart_font.html')



def display(request):
    
    return render(request, 'display.html')



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
    
    return render(request, 'cart_detail.html', {'cart': cart})

    


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



