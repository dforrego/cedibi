from django.contrib import admin
from dashboard.models import Menu, Rol, Company, Profile, Permission


class MenuAdmin(admin.ModelAdmin):
    fields = ['icon', 'name', 'path', 'parent_id', 'enable']
    list_display = ('name', 'path', 'parent_id', 'enable')
    

class RolAdmin(admin.ModelAdmin):
    fields = ['name', 'code']


class CompanyAdmin(admin.ModelAdmin):
    fields = ['name', 'nit', 'logo', 'description', 'status']
    list_display = ('nit', 'name', 'status', 'created_at')
    

class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'rol', 'phone', 'company', 'active']
    # list_display = ('name', 'board', 'state', 'created_at')
    

class PermissionAdmin(admin.ModelAdmin):
    fields = ['rol', 'menu', 'enable']
    # list_display = ('name', 'board', 'state', 'created_at')
  

admin.site.register(Menu, MenuAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Permission, PermissionAdmin)


