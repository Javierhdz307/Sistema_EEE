from django.db import models
from registro.models import Alumno, Personal
from core.models import ExamenTipo
from datetime import date, timedelta
# Create your models here.
class Examen(models.Model):
    ESTADOS = [
        ('realizado', 'Realizado'),
        ('pendiente', 'Pendiente'),
        ('desactualizado', 'Desactualizado'),
    ]
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)
    tipo_examen = models.ForeignKey(ExamenTipo, on_delete=models.SET_NULL, null=True)
    fecha_realizado = models.DateField()
    hora_realizado = models.TimeField()
    archivo_examen = models.FileField(upload_to='examenes/')
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente'  # se puede sobreescribir lógicamente más adelante
    )

    def __str__(self):
        return f"{self.tipo_examen} - {self.alumno.NombreAlumno} {self.alumno.ApellidoAlumno} - {self.fecha_realizado}"
    def actualizar_estado(self):
        if not self.fecha_realizado:
            self.estado = 'pendiente'
            return
        hoy = date.today()
        if (hoy - self.fecha_realizado).days > 365:
            self.estado = 'desactualizado'
        else:
            self.estado = 'realizado'
    
class PAEI(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)
    fecha_realizado = models.DateField()
    hora_realizado = models.TimeField()

    archivo_paei = models.FileField(upload_to='paei/')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"PAEI - {self.alumno.NombreAlumno} {self.alumno.ApellidoAlumno}"