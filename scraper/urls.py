from django.urls import path
from .views import buscar

urlpatterns = [
    path('', buscar, name='buscar'),
]
