from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import secrets
import string
import random

class Usuario(AbstractUser):
    tipo_usuario = models.CharField(max_length=30)
    tipo_documento = models.CharField(max_length=30)
    numero_documento = models.IntegerField()
    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    celular = models.CharField(max_length=12)
    correo_sena = models.CharField(max_length=45)
    area_bienestar = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    def __str__(self):
        return self.area_bienestar
    
class Solicitante(models.Model):
    nombre_solicitante = models.CharField(max_length=120)
    programa_formacion = models.CharField(max_length=100)
    numero_ficha = models.CharField(max_length=15)
    celular = models.CharField(max_length=12)
    correo_sena = models.CharField(max_length=45)
    area_bienestar = models.CharField(max_length=100)  # Esta sería tu "clave foránea lógica"
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitantes', to_field='id')

class Cita(models.Model):  
    fecha = models.DateField()
    hora = models.TimeField()
    estado_cita = models.CharField(max_length=20)
    id_solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE, related_name='cita_solicitante_id', to_field='id')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cita_usuario_id', to_field='id')

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=150)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    lugar_evento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=250)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos', to_field='id')
    def __str__(self):
         return str(self.nombre_evento)