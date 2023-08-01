from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# mahsulotlarni saqlovchi model
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.title
    
# buyurutmalarni saqlovchi model
class Order(models.Model): 
    id = models.AutoField(primary_key=True)
    first_name =models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    phone = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='orders',
    )
    book = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    quantity = models.IntegerField()
    
    
    order_date = models.DateField(auto_now_add=True)
    
    
# korzinkaga vaqtincha saqlovchi model
class Less(models.Model):
    number=models.IntegerField()
    user = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
        related_name='less',
        auto_created=True,
    )
    quantity = models.IntegerField()
    