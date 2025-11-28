from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno
from .forms import AlumnoForm

# Create your views here.
def vista_registros(request):
    tab = request.GET.get("tab", "alumnos")

    alumno_edit = None

    # Si viene GET con ?editar=X -> cargar alumno
    if tab == "alumnos" and "editar" in request.GET:
        alumno_edit = get_object_or_404(Alumno, pk=request.GET["editar"])
    
    # Si es POST -> guardar
    if request.method == "POST" and tab == "alumnos":
        if "editar_id" in request.POST:
            alumno_edit = get_object_or_404(Alumno, pk=request.POST["editar_id"])
            alumno_form = AlumnoForm(request.POST, instance=alumno_edit)
        else:
            alumno_form = AlumnoForm(request.POST)

        if alumno_form.is_valid():
            alumno_form.save()
            return redirect("?tab=alumnos")

    else:
        # Si NO es POST (GET normal)
        if alumno_edit:
            alumno_form = AlumnoForm(instance=alumno_edit)
        else:
            alumno_form = AlumnoForm()

    alumnos = Alumno.objects.all()

    return render(request, "usuarios.html", {
        "tab": tab,
        "alumnos": alumnos,
        "alumno_form": alumno_form,
        "alumno_edit": alumno_edit,
    })