from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from login.models import User, ControlAccess


class ControlAccessAdmin(admin.ModelAdmin):
    fields = ['user', 'ip_address', 'browser']


admin.site.register(User, UserAdmin)
admin.site.register(ControlAccess, ControlAccessAdmin)

