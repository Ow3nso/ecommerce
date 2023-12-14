from datetime import date
from turtle import ondrag
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):

    CHOICES = (
        ('B','Blazers'),
        ('D', 'Dresses'),
        ('G', 'GymWear'),
        ('JA', 'Jackets'),
        ('JE', 'Jeans'),
        ('M', 'Makeups'),
        ('S', 'Shirts'),
        ('SH', 'Shoes'),
        ('O', 'Other')
    )

    img = models.ImageField(upload_to="photos")
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True)
    #description=models.TextField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Inquire(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + " "+ self.message

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    date =models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    item_id = models.CharField(max_length=500, blank=True, null=True)
    product = models.CharField(max_length=500, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=2)
    total = models.IntegerField(blank=True, null=True)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    subtotal = models.PositiveIntegerField()

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    subotal = models.PositiveIntegerField(blank=True, null=True)
    total = models.PositiveIntegerField(blank=True, null=True)
