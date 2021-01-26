from django.db import models

# Create your models here.

class Item:
    name = str()
    price = int()
    rating = int()
    specs = str()
    offer: bool
    url = str()
    img_url = str()

class Customer(models.Model):
    name = models.CharField(max_length= 100)
    search_input = models.CharField(max_length= 100)
