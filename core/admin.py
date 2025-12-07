from django.contrib import admin
from .models import ExamenTipo
from Examenes.models import Examen

# Register your models here.
@admin.register(ExamenTipo)
class ExamenTipoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",) 
# Register your models here.
@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'fecha_realizado', 'personal', 'archivo')
    search_fields = ('alumno__nombre', 'alumno__apellido')
    list_filter = ('fecha_realizado', 'personal')