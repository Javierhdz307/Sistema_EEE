from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from registro.models import Alumno, Personal, AreaPersonal
from registro.forms import AlumnoForm, PersonalForm
from Examenes.models import Examen, PAEI
from .models import Cita
from .forms import CitaForm, ExamenForm, PAEIForm
from django.http import JsonResponse
from django.db.models import Q
# Si luego se agregan tablas y formularios ej:
# from personal.models import Personal
# from personal.forms import PersonalForm
# from alumnos.models import Alumno
# from alumnos.forms import AlumnoForm

# Create your views here.
#       VISTAS PRINCIPALES DEL SISTEMA
#vista menu
class HomeView(LoginRequiredMixin,TemplateView):
    template_name= 'base/home.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
#vista citas
class CitasView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/citas.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        modo = request.GET.get("modo", "agendar")

        # Form principal para agendar
        form = CitaForm()

        # ---------------- FILTROS PARA LISTAR ----------------
        fecha = request.GET.get("fecha")
        hora = request.GET.get("hora")
        alumno_filtro = request.GET.get("alumno")
        personal_filtro = request.GET.get("personal")

        citas = Cita.objects.all().order_by("fecha", "hora")

        if fecha:
            citas = citas.filter(fecha=fecha)
        if hora:
            citas = citas.filter(hora=hora)
        if alumno_filtro:
            citas = citas.filter(alumno__IdAlumno__icontains=alumno_filtro)
        if personal_filtro:
            citas = citas.filter(personal__IdPersonal__icontains=personal_filtro)

        # ---------------- BÚSQUEDA DE ALUMNO PARA AGENDAR ----------------
        alumnos = None
        alumno_query = request.GET.get("alumno_buscar")

        if alumno_query:
            alumnos = Alumno.objects.filter(
                IdAlumno__icontains=alumno_query
            ) | Alumno.objects.filter(
                NombreAlumno__icontains=alumno_query
            )

        return render(request, self.template_name, {
            "modo": modo,
            "form": form,
            "citas": citas,
            "alumnos": alumnos,
            "fecha": fecha or "",
            "hora": hora or "",
            "alumno": alumno_filtro or "",
            "personal": personal_filtro or "",
            "alumno_query": alumno_query or "",
        })

    def post(self, request):
        form = CitaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("citas")

        return render(request, self.template_name, {
            "modo": "agendar",
            "form": form,
            "errores": form.errors
        })
#vista examenes
class ExamenesView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/examenes.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        form = ExamenForm()
        examenes = Examen.objects.all().order_by('-fecha_realizado', '-hora_realizado')
        return render(request, self.template_name, {
            "form": form,
            "examenes": examenes,
        })

    def post(self, request):
        form = ExamenForm(request.POST, request.FILES)
        
        if form.is_valid():
            examen = form.save(commit=False)
            examen.actualizar_estado()
            examen.save()
            return redirect('examenes')   # SOLO si guardó bien
        
        # SI LLEGA AQUÍ ES PORQUE HAY ERRORES
        examenes = Examen.objects.all().order_by('-fecha_realizado', '-hora_realizado')
        return render(request, self.template_name, {
            "form": form,
            "examenes": examenes,
            "errores": form.errors
        })
        
#vista PAEI
class PAEIView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/PAEI.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, *args, **kwargs):
        form = PAEIForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PAEIForm(request.POST, request.FILES)
        if form.is_valid():
            paei = form.save(commit=False)
            paei.actualizar_estado()
            paei.save()
            return redirect('PAEI')

        return render(request, self.template_name, {'form': form})
#vista reportes
class ReportesView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/reportes.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, *args, **kwargs):

        query = request.GET.get("buscar", "").strip()

        alumno = None
        examenes = None
        paei = None

        if query:
            # Buscar por ID o nombre
            alumno = Alumno.objects.filter(
                Q(id__icontains=query) |
                Q(NombreAlumno__icontains=query) |
                Q(ApellidoAlumno__icontains=query)
            ).first()

            if alumno:
                examenes = Examen.objects.filter(alumno=alumno)
                paei = PAEI.objects.filter(alumno=alumno).first()

        return render(request, self.template_name, {
            "alumno": alumno,
            "examenes": examenes,
            "paei": paei,
        })
#vista seguimiento
class SeguimientoView(LoginRequiredMixin,TemplateView):
    template_name= 'paginas/seguimiento.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
#vista ajustes
class AjustesView(LoginRequiredMixin,TemplateView):
    template_name= 'paginas/ajustes.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
#vista ayuda
class AyudaView(LoginRequiredMixin,TemplateView):
    template_name= 'paginas/ayuda.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    #vista usuarios
class UsuariosView(LoginRequiredMixin,TemplateView):
    template_name= 'paginas/usuarios.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        tab = request.GET.get("tab", "alumnos")  # alumnos por defecto

        alumnos = Alumno.objects.all() if tab == "alumnos" else None
        personal = Personal.objects.all() if tab == "personal" else None

        alumno_form = AlumnoForm()
        personal_form = PersonalForm()

        return render(request, self.template_name, {
            "tab": tab,
            "alumnos": alumnos,
            "personal": personal,
            "alumno_form": alumno_form,
            "personal_form": personal_form,
        })

    def post(self, request):
        tab = request.GET.get("tab", "alumnos")

        if tab == "alumnos":
            form = AlumnoForm(request.POST)
        else:
            form = PersonalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(f"/usuarios/?tab={tab}")

        # si hay error en el form, volver a mostrar datos
        alumnos = Alumno.objects.all() if tab == "alumnos" else None
        personal = Personal.objects.all() if tab == "personal" else None

        return render(request, self.template_name, {
            "tab": tab,
            "alumnos": alumnos,
            "personal": personal,
            "alumno_form": AlumnoForm(),
            "personal_form": PersonalForm(),
            "form_errors": form.errors
        })
        
def buscar_alumno(request):
    query = request.GET.get("q", "").strip()

    if not query:
        return JsonResponse({"error": "empty"}, status=400)

    try:
        # Buscar por ID exacto
        alumno = Alumno.objects.filter(id=query).first()

        # Si no es ID, buscar por nombre/apellido
        if not alumno:
            alumno = Alumno.objects.filter(nombre__icontains=query).first()

        if not alumno:
            return JsonResponse({"error": "not_found"}, status=404)

        return JsonResponse({
            "id": alumno.id,
            "nombre": alumno.NombreAlumno,
            "apellido": alumno.ApellidoAlumno,
            "edad": alumno.EdadAlumno,
            "nombreencargado": alumno.EncargadoAlumno
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def buscar_personal(request):
    q = request.GET.get("q", "").strip()

    if not q:
        return JsonResponse({"error": "empty"}, status=400)

    # Buscar por ID primero
    personal = Personal.objects.filter(id=q).first()

    # Si no lo encuentra, buscar por nombre o apellido
    if not personal:
        personal = Personal.objects.filter(nombre__icontains=q).first()

    if not personal:
        personal = Personal.objects.filter(apellido__icontains=q).first()

    if not personal:
        return JsonResponse({"error": "not_found"}, status=404)

    return JsonResponse({
        "id": personal.id,
        "nombre": personal.NombrePersonal,
        "apellido": personal.ApellidoPersonal,
    })
   
def buscar_alumno_paei(request):
    query = request.GET.get("q", "")

    alumnos = Alumno.objects.filter(nombre__icontains=query)[:10]

    data = [
        {
            "nombre": alumno.NombreAlumno,
            "ID": alumno.IdAlumno
        }
        for alumno in alumnos
    ]

    return JsonResponse({"results": data})    
    
def historial_paei(request):
    alumno_id = request.GET.get("alumno_id", None)

    paeis = []
    examenes = []

    if alumno_id:
        paeis = list(PAEI.objects.filter(alumno_id=alumno_id).order_by("-fecha_creacion"))
        examenes = list(Examen.objects.filter(alumno_id=alumno_id).order_by("-fecha"))

    # Convertimos ambos a un formato común para la tabla
    historial = []

    for p in paeis:
        historial.append({
            "tipo": "PAEI",
            "fecha": p.fecha_realizado,
            "personal": p.personal,
            "archivo": p.archivo_paei.url if p.archivo_paei else None,
        })

    for e in examenes:
        historial.append({
            "tipo": "Examen",
            "fecha": e.fecha_realizado,
            "personal": e.personal,
            "archivo": e.archivo_examen.url if e.archivo_examen else None,
        })

    # Ordenar lista combinada por fecha descendente
    historial = sorted(historial, key=lambda x: x["fecha"], reverse=True)

    return render(request, "paginas/reportes.html", {
        "historial": historial,
    })
    
    