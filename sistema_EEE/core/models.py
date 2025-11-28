from django.db import models

# Create your models here.
# Importar Alumno desde app registro
from registro.models import Alumno
from registro.models import Personal


class ExamenTipo(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Cita(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    examen = models.ForeignKey(ExamenTipo, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita de {self.alumno} - {self.examen} a cargo de {self.personal} el {self.fecha} a las {self.hora}"