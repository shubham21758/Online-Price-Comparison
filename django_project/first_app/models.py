from django.db import models

# Create your models here.

class Item:
    id = int()
    name = str()
    price = int()
    rating = int()
    specs = str()
    exchange = str()
    offer: bool
    url = str()
    img_url = str()
