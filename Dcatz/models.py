from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=11) 
    def __str__(self):
        return self.user.username

class AllFiles(models.Model):
    file_name = models.CharField(max_length=2054)
    item_name = models.CharField(max_length=2054)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.item_name}, {self.file_name}"
    
class CatAccessories(models.Model):
    file_name = models.CharField(max_length=2054)
    item_name = models.CharField(max_length=2054)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.item_name}, {self.file_name}"
    
class CatClothing(models.Model):
    file_name = models.CharField(max_length=2054)
    item_name = models.CharField(max_length=2054)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.item_name}, {self.file_name}"
    
class CatFurniture(models.Model):
    file_name = models.CharField(max_length=2054)
    item_name = models.CharField(max_length=2054)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.item_name}, {self.file_name}"
    
class CatFood(models.Model):
    file_name = models.CharField(max_length=2054)
    item_name = models.CharField(max_length=2054)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.item_name}, {self.file_name}"
    
class CatToys(models.Model):
    file_name = models.CharField(max_length=2054)
    item_name = models.CharField(max_length=2054)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.item_name}, {self.file_name}"
    
class CartItems(models.Model):
    cart_item_name = models.CharField(max_length=2054)
    cart_file_name = models.CharField(max_length=2054)
    cart_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.cart_item_name}, {self.cart_file_name}"
    
