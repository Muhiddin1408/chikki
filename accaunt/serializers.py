from rest_framework import serializers

from accaunt.models import User


class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'