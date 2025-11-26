from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroForm

# --- VISTAS DE AUTENTICACIÓN INTEGRADA ---
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView # <--- NUEVA IMPORTACIÓN

# Definición de login_view (para solucionar el error anterior)
login_view = DjangoLoginView.as_view(
    template_name='cuentas/login.html' 
)

# Definición de logout_view (¡SOLUCIONA EL ERROR ACTUAL!)
logout_view = DjangoLogoutView.as_view(
    next_page='/' # Redirige a la página de inicio (o a donde desees) después de cerrar sesión
)

# VISTA DE REGISTRO
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, "Registro exitoso, bienvenido!")
            return redirect("dashboard")
    else:
        form = RegistroForm()
    
    return render(request, "cuentas/registro.html", {"form": form})