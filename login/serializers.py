from django.contrib.auth import authenticate
from rest_framework import serializers
from login.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]
        

class LoginSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    login = serializers.CharField()
    password = serializers.CharField()

    def get_authenticated_user(self):
        data = self.validated_data
        kwargs = {
            'username': data['login'],
            'password': data['password'],
        }
        user = authenticate(**kwargs)
        return user
