import uuid
from django.db import models


# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    mensaje = models.CharField(max_length=130, null=False)    
    def __str__(self) -> str:
        return self.nombre

class Flan(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField()
    ingredientes= models.TextField(default = False)
    precio = models.IntegerField(default=1000)
    foto = models.URLField()
    is_private = models.BooleanField(default = False)
    def __str__(self) -> str:
        return self.nombre