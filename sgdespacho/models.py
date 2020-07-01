from django.db import models

# Create your models here.
class Paquete(models.Model):
    nombre=models.CharField (max_length=255)
    categoria=models.CharField(max_length=255)
    precio=models.IntegerField()
    fecha=models.DateField()
    

class Bodega(models.Model):
    nombre_cliente=models.CharField(max_length=255)
    monto= models.IntegerField()
    idpaquete=models.ForeignKey('Paquete',on_delete=models.CASCADE)

class Boleta (models.Model):
    nombre_cliente=models.CharField(max_length=45)
    rut_cliente= models.CharField(max_length=45)
    direccion_cliente=models.CharField(max_length=45)
    correo_cliente=models.CharField(max_length=45)
