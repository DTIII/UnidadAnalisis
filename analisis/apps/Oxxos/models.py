from django.db import models

# Create your models here.
class sqlServerConn(models.Model):
    Id=models.IntegerField()
    Sucursal=models.TextField()
    Direccion=models.TextField()
    Latitud=models.CharField(max_length=50)
    Longitud=models.CharField(max_length=50)
    Estatus=models.CharField(max_length=10)
    FechaAlta=models.DateField()