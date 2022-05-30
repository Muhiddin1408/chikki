from django.db import models

# Create your models here.
from accaunt.models import User


class Restorant(models.Model):
    name = models.CharField(max_length=125)
    address = models.CharField(max_length=125)
    image = models.ImageField(upload_to="restorant")
    start_date = models.TimeField(blank=True, null=True)
    finish_date = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Product(models.Model):
    measure = [
        ('dona', 'dona'),
        ('kg', 'kg'),
        ('litr', 'litr'),
        ('metr', 'metr')
    ]
    name = models.CharField(max_length=125)
    restaurant = models.ForeignKey(Restorant, on_delete=models.CASCADE)
    price = models.FloatField()
    measurement = models.CharField(max_length=125, choices=measure)
    text = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    preparation_time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.username + ' ' +self.product.name


