from django.contrib import admin
from .models import ExamenTipo
from Examenes.models import Examen, PAEI

# Register your models here.
@admin.register(ExamenTipo)
class ExamenTipoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",) 
# Register your models here.
@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'tipo_examen', 'fecha_realizado', 'personal', 'estado', 'archivo_link')

    def archivo_link(self, obj):
        if obj.archivo_examen:
            return f"<a href='{obj.archivo_examen.url}' target='_blank'>Ver archivo</a>"
        return "Sin archivo"
    archivo_link.allow_tags = True
    archivo_link.short_description = "Archivo"

@admin.register(PAEI)
class PAEIAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'fecha_realizado', 'personal', 'estado', 'archivo_link')

    def archivo_link(self, obj):
        if obj.archivo_paei:
            return f"<a href='{obj.archivo_paei.url}' target='_blank'>Ver archivo</a>"
        return "Sin archivo"
    archivo_link.allow_tags = True
    archivo_link.short_description = "Archivo"