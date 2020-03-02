from django.db import models
from dashboard.models import Company


class LogFiles(models.Model):
    name = models.CharField(max_length=40)
    datetime = models.DateTimeField()
    ip_address = models.CharField(max_length=20)
    result = models.CharField(max_length=3)
    message = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

