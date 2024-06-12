from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cart_font', views.cart_font, name="cart_font"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('display', views.display, name="display"),
 
    path('checkout', views.checkout, name='checkout'),

    path('order_id/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
   
   
]







