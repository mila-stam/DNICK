from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"
    

class Market(models.Model):
    name = models.CharField(max_length=100)
    #personal
    #proizvodi
    numMarket = models.IntegerField()
    dateOpening = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    openFrom = models.DateTimeField()
    openTo = models.DateTimeField()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    embg = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Product(models.Model):
    type_choices = {
        "f": "Food",
        "d": "Drink",
        "b": "Bakery",
        "c": "Cosmetics",
        "h": "Hygiene"
    }

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=type_choices)
    isHomemade = models.BooleanField()
    code = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class MarketProduct(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    

