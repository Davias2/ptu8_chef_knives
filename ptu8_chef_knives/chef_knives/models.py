from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=350)
    blade_length = models.IntegerField(default=0)

    def __str__(self) :
        return self.name
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) :
        return f"{self.user.username}'s profile"
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('C', 'Cancelled')
    )

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self) :
        return str(self.id)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.user.username}'s cart item #{self.id}"
        

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
