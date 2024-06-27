from django.db import models

# Create your models here.
class Project(models.Model):
    presupuesto = models.BigIntegerField()
    unidad = models.CharField(max_length=100)
    TipoBien = models.CharField(max_length=50)
    Cantidad = models.IntegerField()
    ValorUnit = models.BigIntegerField()
    ValorTot = models.BigIntegerField()
    Fecha = models.DateField()
    Proveedor = models.CharField(max_length=60)
    Documen = models.TextField(max_length=200)
