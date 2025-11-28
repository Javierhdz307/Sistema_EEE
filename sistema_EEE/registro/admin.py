from django.contrib import admin
from .models import Alumno, Personal, AreaPersonal

# Register your models here.
@admin.register(AreaPersonal)
class AreaPersonalAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("IdAlumno", "NombreAlumno", "ApellidoAlumno", "EdadAlumno", "Activo")
    list_filter = ("Activo","IdAlumno", "NombreAlumno")
    search_fields = ("IdAlumno", "NombreAlumno", "ApellidoAlumno")


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ("IdPersonal", "NombrePersonal", "ApellidoPersonal", "AreaPersonal", "Activo")
    list_filter = ("Activo", "AreaPersonal","NombrePersonal")
    search_fields = ("IdPersonal", "NombrePersonal", "ApellidoPersonal")