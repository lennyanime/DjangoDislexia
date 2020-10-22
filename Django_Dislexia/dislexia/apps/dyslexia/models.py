from django.db import models

# Create your models here.

class Especialista(models.Model):
    id_especialista=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, blank=False, null=False)
    profesion=models.CharField(max_length=50, blank=False, null=False)

class Niño(models.Model):
    id_niño=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, blank=False, null=False)
    edad=models.IntegerField(null=False)
    especialista=models.ForeignKey(Especialista, null=False, on_delete=models.CASCADE)

class Diagnostico(models.Model):
    id_diagnostico=models.AutoField(primary_key=True)
    resultado=models.CharField(max_length=8, blank=False, null=False)
    descripcion=models.CharField(max_length=50, blank=False, null=False)
    especialista=models.ForeignKey(Especialista, null=False, on_delete=models.CASCADE)