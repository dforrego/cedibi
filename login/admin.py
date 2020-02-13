from django.contrib import admin
from login.models import User, ControlAccess


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'email']
    list_display = ('username', 'email', 'updated_at')


class ControlAccessAdmin(admin.ModelAdmin):
    fields = ['user', 'ip_address', 'browser']


admin.site.register(User, UserAdmin)
admin.site.register(ControlAccess, ControlAccessAdmin)