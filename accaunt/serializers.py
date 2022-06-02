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
        fields = [
            'id',
            'name',
            'image',
            'get_all_type',
            'star'
        ]


class RestaurantSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    restaurant_image = serializers.ReadOnlyField(source='restaurant.image.url')
    class Meta:
        model = Product
        fields = (
            'name',
            'restaurant',
            'restaurant_image',
            'price',
            'text',
        )


class RestaurantSerializerTest(serializers.ModelSerializer):
    # restaurant = serializers.ReadOnlyField(source='restaurant.name')
    # restaurant_image = serializers.ReadOnlyField(source='restaurant.image.url')

    class Meta:
        model = Restorant
        fields = [
            'name',
            'image',
            'get_all_products',
        ]

    def to_representation(self, instance):
        print(instance, 'id')
        data = super().to_representation(instance)
        print(data)
        # data['get_all_products'] = ProductFilialBaseSerializer(instance=instance.product).data
        products = data['get_all_products']
        for p in products:
            if p.get('type') :
                print(p.get('type'))




class ProductSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    # type = serializers.ReadOnlyField(source='type.na')

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


# class StarSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Star
#         fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


