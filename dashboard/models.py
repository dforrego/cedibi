from django.db import models
from login.models import User


def user_directory_path(instance, filename):
    return 'company_{0}/{1}'.format(instance.nit, filename)


class Menu(models.Model):
    icon = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    path = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    enable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Rol(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()
    permission = models.ManyToManyField(
        Menu,
        through='Permission',
        through_fields=('rol', 'menu'),
    )
    
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    nit = models.CharField(max_length=9)
    logo = models.ImageField(upload_to=user_directory_path)
    description = models.CharField(max_length=9)
    status = models.BooleanField(default=True)
    contact_name = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=40)
    contact_phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    phone = models.CharField(max_length=12)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    group = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)


class Permission(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='+')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    enable = models.BooleanField(default=True)
