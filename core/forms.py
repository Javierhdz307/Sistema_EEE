from django import forms
from .models import Cita, ExamenTipo
from registro.models import Alumno,Personal
from Examenes.models import Examen, PAEI


class CitaForm(forms.ModelForm):
    alumno = forms.ModelChoiceField(
        queryset=Alumno.objects.all(),
        label="Alumno",
        widget=forms.Select(attrs={'class': 'input-form'})
    )
    examen = forms.ModelChoiceField(
        queryset=ExamenTipo.objects.all(),
        label="Tipo de examen",
        widget=forms.Select(attrs={'class': 'input-form'})
    )  
    personal = forms.ModelChoiceField(
        queryset=Personal.objects.all(),
        label="Personal",
        widget=forms.Select(attrs={'class': 'input-form'})
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'input-form'
        }),
        label="Fecha de la cita"
    )
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'input-form'
        }),
        label="Hora de la cita"
    )

    class Meta:
        model = Cita
        fields = ['alumno', 'examen', 'personal', 'fecha', 'hora']
        
class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['alumno', 'personal', 'tipo_examen',
                  'fecha_realizado', 'hora_realizado',
                  'archivo_examen', 'observaciones']

        widgets = {
            'alumno': forms.Select(attrs={'class': 'btn-editar'}),
            'personal': forms.Select(attrs={'class': 'btn-editar'}),
            'tipo_examen': forms.Select(attrs={'class': 'btn-editar'}),
            'fecha_realizado': forms.DateInput(attrs={'type': 'date','class': 'btn-editar'}),
            'hora_realizado': forms.TimeInput(attrs={'type': 'time','class': 'btn-editar'}),
            'archivo_examen': forms.ClearableFileInput(attrs={'class': 'btn-editar'}),
            'observaciones': forms.Textarea(attrs={'class': 'btn-editar'}),
        }
class PAEIForm(forms.ModelForm):
    fecha_realizado = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'btn-editar'
        })
    )

    hora_realizado = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'btn-editar'
        })
    )

    class Meta:
        model = PAEI
        fields = [
            'alumno',
            'personal',
            'fecha_realizado',
            'hora_realizado',
            'archivo_paei',
            'observaciones',
        ]
        widgets = {
            'alumno': forms.Select(attrs={'class': 'btn-editar'}),
            'personal': forms.Select(attrs={'class': 'btn-editar'}),
            'archivo_paei': forms.ClearableFileInput(attrs={'class': 'btn-editar'}),
            'observaciones': forms.Textarea(attrs={'class': 'btn-editar'}),
        }