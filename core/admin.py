from django.contrib import admin
from .models import ExamenTipo

# Register your models here.
@admin.register(ExamenTipo)
class ExamenTipoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",) 
# Register your models here.
