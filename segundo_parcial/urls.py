from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# CAMBIA ESTA LÍNEA:
# from cuentas.views import login_view 
from cuentas.views import registro # <--- IMPORTA LA VISTA 'registro'

from alumnos.views import dashboard

def home(request):
    return HttpResponse("<h1>Bienvenido al Segundo Parcial</h1><p>Todo funciona.</p>")

urlpatterns = [
    # CAMBIA ESTA LÍNEA:
    path('', registro, name="home"), # <--- Usa 'registro' en lugar de 'login_view'
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),
    path('alumnos/', include('alumnos.urls')),
    path('scraper/', include('scraper.urls')),
    path('dashboard/', dashboard, name="dashboard"),
]
