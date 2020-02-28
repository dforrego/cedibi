from django.contrib.auth import authenticate
from rest_framework import serializers
from dashboard.serializers import CompanyUserSerializer, RolSerializer
from login.models import User


class UserSerializer(serializers.ModelSerializer):
    profile = CompanyUserSerializer(many=False, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile']


class ProfileSerializer(serializers.ModelSerializer):
    rol = RolSerializer(many=False, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'rol']
        

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
