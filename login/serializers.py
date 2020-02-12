from rest_framework import serializers
from login.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'created_at']