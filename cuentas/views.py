from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.contrib import messages

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Registro exitoso, inicia sesión.")
            return redirect("login")
    else:
        form = RegistroForm()

    return render(request, "cuentas/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Credenciales incorrectas.")

    return render(request, "cuentas/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
