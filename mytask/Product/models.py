from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name




# Trial Test
   
    
class Order(models.Model):
    username = models.CharField(max_length=50, default='username')
    first_name = models.CharField(max_length=50, default='first_name')
    last_name = models.CharField(max_length=50, default='last_name')
    company_name = models.CharField(max_length=100, default='company_name')
    address = models.TextField(default=False)
    house_number_street_name = models.CharField(max_length=100, default=1)
    town_city = models.CharField(max_length=50, default=1)
    country = models.CharField(max_length=50, default=1)
    postcode_zip = models.CharField(max_length=20, default=1)
    mobile = models.CharField(max_length=20, default=1)
    email_address = models.EmailField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=False)
    payment_method = models.CharField(max_length=200, default='card')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    create_account = models.BooleanField(default=False)
   
    
    # ship_to_different_address = models.BooleanField(default=False)


    def calculate_total_price(self):
       
        items = self.orderitem_set.all()
        total_price = sum(item.price * item.quantity for item in items)
        return total_price

       
    def  __str__(self):
        return 'Order {}'.format(self.id)
    
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())    
      


    
    
class OrderItem(models.Model):
   
     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
     product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, default=True)
     quantity = models.PositiveIntegerField(default=1)
     price = models.DecimalField(max_digits=10, decimal_places=2, default=False)
     total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
     
    
     def __str__(self):
             return '{}'.format(self.id)
         
     def get_cost(self):
            return self.price * self.quantity
        

        
    
    








