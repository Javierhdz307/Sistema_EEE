from django import forms
from .models import Alumno, Personal

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            "IdAlumno",
            "NombreAlumno",
            "ApellidoAlumno",
            "EdadAlumno",
            "EncargadoAlumno",
            "Activo",
        ]
        widgets = {
            "IdAlumno": forms.TextInput(attrs={"class": "input"}),
            "NombreAlumno": forms.TextInput(attrs={"class": "input"}),
            "ApellidoAlumno": forms.TextInput(attrs={"class": "input"}),
            "EdadAlumno": forms.NumberInput(attrs={"class": "input"}),
            "EncargadoAlumno": forms.TextInput(attrs={"class": "input"}),
            "Activo": forms.CheckboxInput(attrs={"class": "checkbox"}),
        }

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ["IdPersonal", "NombrePersonal", "ApellidoPersonal", "AreaPersonal","Activo",]
        widgets = {
            "IdPersonal": forms.TextInput(attrs={"class": "input"}),
            "NombrePersonal": forms.TextInput(attrs={"class": "input"}),
            "ApellidoPersonal": forms.TextInput(attrs={"class": "input"}),
            "AreaPersonal": forms.Select(attrs={"class": "input"}),
            "Activo": forms.CheckboxInput(attrs={"class": "checkbox"}),
        }