from rest_framework import serializers
from dashboard.models import Menu, Company, Profile, Rol
from bi.serializers import BoardListSerializer


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['icon', 'name', 'path', 'parent_id', 'enable']


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['name', 'code']


class BoardsByRolSerializer(serializers.ModelSerializer):
    board = BoardListSerializer(many=True, read_only=False)

    class Meta:
        model = Rol
        fields = ['name', 'boards']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'nit', 'logo', 'description', 'status']
      
      
class CompanyUserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    rol = BoardsByRolSerializer(many=False, read_only=True)
    
    class Meta:
        model = Profile
        fields = ['company', 'rol']


class RolUserSerializer(serializers.ModelSerializer):
    rol = RolSerializer(many=False, read_only=True)
    
    class Meta:
        model = Profile
        fields = ['rol']


