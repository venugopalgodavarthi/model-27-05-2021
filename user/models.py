from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique = True)
    phone = models.IntegerField(unique = True)
    address = models.CharField(max_length = 50)
    
class Product1(models.Model):
    pname = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.FloatField()
    
class Transition(models.Model):
    tdate = models.DateField()
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product1, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    
    
    
    
    
