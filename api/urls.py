from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accaunt.views import *
from chikkiconf import settings
#
router = DefaultRouter()
router.register('home', Home)
router.register('product', ProductViewset, basename='product')
router.register('order', OrderViewset, basename='order')


urlpatterns = [
    path('register/', register),

    path('register_accepted/', register_accepted),
    path('', include(router.urls)),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)