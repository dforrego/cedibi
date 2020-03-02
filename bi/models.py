from django.db import models
from dashboard.models import Rol
from login.models import User


class TypeBoard(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()
    
    class Meta:
        verbose_name = "Tipos de Tablero"
        
    def __str__(self):
        return self.name
    

class Board(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    type = models.ForeignKey(TypeBoard, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    rol = models.ManyToManyField(Rol, related_name='boards')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    
    class Meta:
        verbose_name = "Tablero"
      
    def __str__(self):
        return self.name


class Comment(models.Model):
    message = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Comentario"
      

class Values(models.Model):
    val_x = models.IntegerField()
    val_y = models.IntegerField()
    nam_x = models.CharField(max_length=15)
    nam_y = models.CharField(max_length=15)
    percent = models.IntegerField()
    
    class Meta:
        verbose_name = "Valores del gráfico"
    

class Graph(models.Model):
    name = models.CharField(max_length=40)
    values = models.ManyToManyField(Values)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    
    class Meta:
        verbose_name = "Gráfico"
