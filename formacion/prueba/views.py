from django.shortcuts import render

# Create your views here.

from .models import Aprendiz

def lista_aprendices(request):

    aprendices = Aprendiz.objects.all()

    contexto = {
        'aprendices': aprendices
    } 
    return render(request, 'prueba/index.html', contexto)