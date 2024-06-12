from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Carts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class OrderItem(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    
    
    
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='first_name')
    last_name = models.CharField(max_length=50, default='last_name')
    company_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(default=False)
    house_number_street_name = models.CharField(max_length=100, default=1)
    town_city = models.CharField(max_length=50, default=1)
    country = models.CharField(max_length=50, default=1)
    postcode_zip = models.CharField(max_length=20, default=1)
    mobile = models.CharField(max_length=20, default=1)
    email_address = models.EmailField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=False)
    payment_method = models.CharField(max_length=200, default='card')
    # created_at = models.DateTimeField(auto_now_add=True, default=1)
    # updated_at = models.DateTimeField(auto_now=True, default=1)

    # def __str__(self):
    #     return f"Order {self.id} by {self.user.username}   

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     shipping_address = models.CharField(max_length=255)
#     billing_address = models.CharField(max_length=255)
#     payment_method = models.CharField(max_length=50, default='Credit-Card/Debit-Card')
    
    
    

    def get_absolute_url(self):
          return reverse("course:verify-payment", kwargs={
            "ref": self.ref,
        })











# class Carts(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
    

   

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     shipping_address = models.TextField()
#     billing_address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)