from django.db import models

# Create your models here.
class Pc(models.Model):
    modelo = models.CharField(max_length=10)
    fecha = models.DateTimeField()