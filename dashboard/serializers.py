from rest_framework import serializers
from dashboard.models import Menu, Company, Profile, Rol


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['icon', 'name', 'path', 'parent_id', 'enable']


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['name', 'code']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'nit', 'logo', 'description', 'status']
      
      
class CompanyUserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    rol = RolSerializer(many=False, read_only=True)
    
    class Meta:
        model = Profile
        fields = ['company']


class RolUserSerializer(serializers.ModelSerializer):
    rol = RolSerializer(many=False, read_only=True)
    
    class Meta:
        model = Profile
        fields = ['rol']


