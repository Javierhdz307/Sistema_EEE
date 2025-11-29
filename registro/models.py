from django.db import models

# Create your models here.
# --------------------------------------
#   Modelo de Áreas del Personal
# --------------------------------------
class AreaPersonal(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Área del Personal"
        verbose_name_plural = "Áreas del Personal"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# --------------------------------------
#   Modelo Alumno
# --------------------------------------
class Alumno(models.Model):
    IdAlumno = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="ID del Alumno",
        help_text="Identificador institucional del alumno."
    )
    NombreAlumno = models.CharField(max_length=100)
    ApellidoAlumno = models.CharField(max_length=100)
    EdadAlumno = models.PositiveIntegerField()
    EncargadoAlumno = models.CharField(max_length=150)

    # Nuevo campo
    Activo = models.BooleanField(
        default=True,
        verbose_name="¿Activo?",
        help_text="Indica si el alumno está activo en la institución."
    )

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ['ApellidoAlumno', 'NombreAlumno']

    def __str__(self):
        estado = "Activo" if self.Activo else "Inactivo"
        return f"{self.NombreAlumno} {self.ApellidoAlumno} ({self.IdAlumno}) - {estado}"


# --------------------------------------
#   Modelo Personal
# --------------------------------------
class Personal(models.Model):
    IdPersonal = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="ID del Personal",
        help_text="Código institucional del miembro del personal."
    )
    NombrePersonal = models.CharField(max_length=100)
    ApellidoPersonal = models.CharField(max_length=100)
    AreaPersonal = models.ForeignKey(
        AreaPersonal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="personal",
        verbose_name="Área"
    )

    # Nuevo campo
    Activo = models.BooleanField(
        default=True,
        verbose_name="¿Activo?",
        help_text="Indica si el miembro del personal sigue prestando servicio."
    )

    class Meta:
        verbose_name = "Miembro del Personal"
        verbose_name_plural = "Personal"
        ordering = ['ApellidoPersonal', 'NombrePersonal']

    def __str__(self):
        area = f" - {self.AreaPersonal}" if self.AreaPersonal else ""
        estado = "Activo" if self.Activo else "Inactivo"
        return f"{self.NombrePersonal} {self.ApellidoPersonal} ({self.IdPersonal}){area} - {estado}"