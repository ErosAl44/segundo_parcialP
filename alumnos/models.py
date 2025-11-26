from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nombre
