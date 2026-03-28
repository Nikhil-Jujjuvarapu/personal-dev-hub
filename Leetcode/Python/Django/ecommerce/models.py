from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='product')
    tag = models.ManyToManyField(Tag,related_name='product')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order {self.id}'

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()




