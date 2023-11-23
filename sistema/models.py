from django.db import models

# Create your models here.

class Soportet(models.Model):
    codigo=models.CharField(primary_key=True,max_length=50)
    nombre=models.CharField(max_length=50)
    serie=models.CharField(max_length=60)
    procesador=models.Charfield(max_length=100)

    
