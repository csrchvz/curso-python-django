from django.shortcuts import render, render_to_response
from .models import *
# Create your views here.

def principal(request):
    return render_to_response("app/index.html", locals())

def alumnos(request):
    alumnos = Estudiante.objects.all()
    return render_to_response("app/alumnos.html", locals())