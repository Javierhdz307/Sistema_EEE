from django.db import models
from registro.models import Alumno, Personal
from core.models import ExamenTipo
# Create your models here.
class Examen(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)
    tipo_examen = models.ForeignKey(ExamenTipo, on_delete=models.SET_NULL, null=True)
    fecha_realizado = models.DateField()
    hora_realizado = models.TimeField()
    archivo_examen = models.FileField(upload_to='examenes/')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_examen} - {self.alumno.NombreAlumno} {self.alumno.ApellidoAlumno} - {self.fecha_realizado}"
    
class PAEI(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)
    fecha_realizado = models.DateField()
    hora_realizado = models.TimeField()

    archivo_paei = models.FileField(upload_to='paei/')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"PAEI - {self.alumno.NombreAlumno} {self.alumno.ApellidoAlumno}"