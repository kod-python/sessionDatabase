from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from .cart import Cart
from .models import Product
from django.contrib import messages
from .models import  Order, OrderItem
from django.core.mail import send_mail
from django.contrib.auth.models import User
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
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save()
            
          
            if form.cleaned_data.get('create_account'):
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email_address')
                password = User.objects.make_random_password()
                
                try:
                    
                    user = User.objects.create_user(
                        username=username,      
                        email=email, 
                        password=password,
                        first_name=form.cleaned_data.get('first_name'),
                        last_name=form.cleaned_data.get('last_name')
                    )
                    user.save()
                    
                    print(user)
                    
                    send_mail(
                        'Your Account Details',
                        f'Hello {user.first_name},\n\nYour account has been created. Your username is: {username} and your password is: {password}\n\nPlease change your password after logging in for the first time.\n\nThank you!',
                        'krist_table@yahoo.com', 
                        [email],
                        fail_silently=False,
                    )
                    
                    print(send_mail)
                     
                except Exception as e:
                  
                    print(f"Error creating user or sending email: {e}")
   
        
            
          
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                   
                    product = item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    total_price=item['total_price']              
                   
             )
     
            
            cart.clear()      
                   
        
            return redirect('order_confirmation', order_id=order.id, )
    else:
        
        form = CheckoutForm()
        
    return render(request, 'checkout.html', {'form':form, 'cart':cart})





















# def checkout(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             order = form.save()
            
            
#     #    FOR USER CREATION AND DONT HAVE A USER AUTHENTICATION YET 
    
#             if form.cleaned_data['create_account']:
#                 username = form.cleaned_data['username']
#                 email = form.cleaned_data['email_address']
#                 password = User.objects.make_random_password()
            
#                 user = User.objects.create_user(
#                     username=username,      
#                     email=email, 
#                     password=password,
#                     first_name=form.cleaned_data['first_name'],
#                     last_name=form.cleaned_data['last_name']
#                 )
#                 user.save()   
                   
#                 #   send_welcome_email(user)
#                 #   assign_default_permissions(user)

#                 # Send email with account details
#                 send_mail(
#                     'Your Account Details',
#                     f'Your account has been created. Your password is: {password}',
#                     'from@example.com',  # Replace with your from email
#                     [email],
#                     fail_silently=False,
#                 )
                
#                 print(send_mail)
        
            
          
#             for item in cart:
#                 OrderItem.objects.create(
#                     order=order,
                   
#                     product = item['product'],
#                     price=item['price'],
#                     quantity=item['quantity'],
#                     total_price=item['total_price']              
                   
#              )
     
            
#             cart.clear()      
                   
        
#             return redirect('order_confirmation', order_id=order.id, )
#     else:
        
#         form = CheckoutForm()
        
#     return render(request, 'checkout.html', {'form':form, 'cart':cart})






        

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





# Pages Site


def login(request):
    
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            return redirect('/')
        else:
            messages.info(request, 'credentials are incorrect')
            return redirect('login')
    else:       
    
     return render(request, 'login.html')



def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password == password2:
            # if User.objects.filter(email=email).exists():
            #     messages.info(request, 'email already exists')
            #     return redirect('register')
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please login.')
                # User.save()
                return redirect('login')
        else:
            messages.error(request, 'passowrd not matched')
     
            return redirect('register')
        
    else:    
    
    
    
    
     return render(request, 'signup.html')