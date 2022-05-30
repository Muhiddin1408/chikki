from django.conf.urls.static import static
from django.urls import path

from accaunt.views import *
from chikkiconf import settings

urlpatterns = [
    path('register/', register),
    path('register_accepted/', register_accepted),
    # path('', ),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)