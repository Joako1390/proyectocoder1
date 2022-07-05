from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.


def curso(self):
    
    curso= Curso(nombre="Django")
    curso.save()
    texto= f"Curso creado: {curso.nombre}"
    return HttpResponse(texto)