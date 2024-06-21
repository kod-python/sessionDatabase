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
    username = models.CharField(max_length=50, default='Username')
    first_name = models.CharField(max_length=50, default='First_Name')
    last_name = models.CharField(max_length=50, default='Last_Name')
    company_name = models.CharField(max_length=100, default='Company_Name')
    address = models.TextField(default='Address')
    house_number_street_name = models.CharField(max_length=100, default='House_Number')
    town_city = models.CharField(max_length=50, default='Town/City')
    country = models.CharField(max_length=50, default='Country')
    postcode_zip = models.CharField(max_length=20, default='Post')
    mobile = models.CharField(max_length=20, default='Mobile')
    email_address = models.EmailField(default='Email')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default='Ghc')
    payment_method = models.CharField(max_length=200, default='Card')
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
     price = models.DecimalField(max_digits=10, decimal_places=2, default='Price')
     total_price = models.DecimalField(max_digits=10, decimal_places=2,  null=True)
     
    
     def __str__(self):
             return '{}'.format(self.id)
         
     def get_cost(self):
            return self.price * self.quantity
        

        
    
    








