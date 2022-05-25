from django.urls import path, include

from accaunt.views import register, register_accepted

urlpatterns = [
    path('register/', register),
    path('register_accepted/', register_accepted),
]