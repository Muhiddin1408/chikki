from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(Restorant)
admin.site.register(Product)
admin.site.register(Type)