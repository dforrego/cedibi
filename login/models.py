from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    
    def __str__(self):
        return self.username
    
    
class ControlAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ip_address = models.CharField(max_length=50)
    browser = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
