from django.urls import path
from .views import dashboard, crear_alumno, enviar_pdf

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('crear/', crear_alumno, name='crear_alumno'),
    path('<int:pk>/pdf/', enviar_pdf, name='enviar_pdf'),
]
