from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    document_type = models.CharField(max_length=2)
    document_id = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class ControlAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ip_address = models.CharField(max_length=50)
    browser = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
