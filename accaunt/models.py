from django.contrib.auth.models import AbstractUser
from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
# from location_field.models.spatial import LocationField


class User(AbstractUser):
    # phone = models.IntegerField(blank=True, null=True, unique=True)
    # username = models.(max_length=125, unique=False)
    sms_code = models.IntegerField(blank=True, null=True)
    sms_status = models.BooleanField(default=False)
    city = models.CharField(max_length=100,blank=True, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True, null=True)

    # USERNAME_FIELD = 'phone'


