from rest_framework import serializers

from accaunt.models import User
from api.models import Restorant


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
