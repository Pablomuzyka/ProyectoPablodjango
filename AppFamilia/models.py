from platform import freedesktop_os_release
from django.db import models

# Create your models here.


class familiar(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad=models.IntegerField()
    dni=models.IntegerField()