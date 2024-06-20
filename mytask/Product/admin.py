from django.contrib import admin

from .models import Product
# from .models import Order, OrderItem, Carts

from .models import OrderItem, Order

# Register your models here.




class OrderItemInline(admin.TabularInline):
     model = OrderItem
     raw_id_fields = ['product']
     
     
     
class OrderAdmin(admin.ModelAdmin):
     list_display = ['id','first_name', 'last_name', 'company_name', 'address', 'house_number_street_name', 'town_city', 'country', 'postcode_zip', 'mobile', 'email_address','payment_method', 'total_price']
      
     list_filter = [ 'updated', 'created']
     inlines = [OrderItemInline]
   








admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderAdmin)

# admin.site.register(OrderItem)
# admin.site.register(Carts)

# admin.site.register(OrderItem)
# admin.site.register(Carts)
