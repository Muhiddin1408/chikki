from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=125)

