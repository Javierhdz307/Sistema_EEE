from django.urls import path
from .views import HomeView, CitasView, ExamenesView, PAEIView, ReportesView, SeguimientoView, AjustesView, AyudaView, UsuariosView,buscar_alumno, buscar_personal,historial_paei,buscar_alumno_paei
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('citas/', CitasView.as_view(), name='citas'),
    path('examenes/', ExamenesView.as_view(), name='examenes'),
    path('PAEI/', PAEIView.as_view(), name='PAEI'),
    path('reportes/', ReportesView.as_view(), name='reportes'),
    path('seguimiento/', SeguimientoView.as_view(), name='seguimiento'),
    path('ajustes/', AjustesView.as_view(), name='ajustes'),
    path('ayuda/', AyudaView.as_view(), name='ayuda'),
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("citas/buscar-alumno/", buscar_alumno, name="buscar_alumno"),
    path('citas/buscar-personal/', buscar_personal, name='buscar_personal'),
    path("paei/historial/", historial_paei, name="historial_paei"),
    path("paei/buscar-alumno/", buscar_alumno_paei, name="buscar_alumno_paei"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)