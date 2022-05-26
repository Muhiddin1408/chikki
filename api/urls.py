from django.conf.urls.static import static
from django.urls import path

from accaunt.views import register, register_accepted
from chikkiconf import settings

urlpatterns = [
    path('register/', register),
    path('register_accepted/', register_accepted),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)