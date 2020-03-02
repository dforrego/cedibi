from django.contrib import admin
from bi.models import TypeBoard, Board, Comment, Values, Graph


class TypeBoardAdmin(admin.ModelAdmin):
    fields = ['name', 'code']


class BoardAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'type', 'status', 'rol']
    list_display = ('name', 'description', 'type', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    fields = ['message', 'user', 'board']
    list_display = ('message', 'user', 'board', 'created_at')


class ValuesAdmin(admin.ModelAdmin):
    fields = ['val_x', 'val_y', 'nam_x', 'nam_y', 'percent']


class GraphAdmin(admin.ModelAdmin):
    fields = ['name', 'values', 'board', 'state']
    list_display = ('name', 'board', 'state', 'created_at')
  

admin.site.register(TypeBoard, TypeBoardAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Values, ValuesAdmin)
admin.site.register(Graph, GraphAdmin)
