from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    mensaje = models.CharField(max_length=130)
