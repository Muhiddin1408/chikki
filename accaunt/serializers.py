from rest_framework import serializers

from accaunt.models import User
from api.models import *


class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name'
        )


class RestorantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restorant
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    restaurant_image = serializers.ReadOnlyField(source='restaurant.image')
    class Meta:
        model = Product
        fields = (
            'name',
            'restaurant',
            'restaurant_image',
            'price',
            'text',
        )


class ProductSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    type = serializers.ReadOnlyField(source='type.name')

    class Meta:
        model = Product
        fields = (
            'name',
            'restaurant',
            'type',
            'image',
            'price',
            'measurement',
            'text',
            'status',
            'preparation_time',

        )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


