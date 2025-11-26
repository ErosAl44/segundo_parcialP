from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AlumnoForm
from .models import Alumno
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import EmailMessage

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def dashboard(request):
    alumnos = Alumno.objects.filter(usuario=request.user)
    return render(request, "alumnos/dashboard.html", {"alumnos": alumnos})

@login_required
def crear_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        alumno = form.save(commit=False)
        alumno.usuario = request.user
        alumno.save()
        return redirect('dashboard')
    return render(request, 'alumnos/form.html', {'form': form})

@login_required
def enviar_pdf(request, pk):
    alumno = Alumno.objects.get(pk=pk, usuario=request.user)

    # Generar PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{alumno.nombre}.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Alumno: {alumno.nombre}")
    p.drawString(100, 780, f"Curso: {alumno.curso}")
    p.drawString(100, 760, f"Nota: {alumno.nota}")
    p.showPage()
    p.save()

    # Enviar por correo
    email = EmailMessage(
        subject="PDF del alumno",
        body="Adjunto PDF",
        from_email="no-reply@miapp.com",
        to=[request.user.email]
    )
    email.attach(f"{alumno.nombre}.pdf", response.getvalue(), "application/pdf")
    email.send()

    return redirect("dashboard")
