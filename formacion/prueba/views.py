from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Aprendiz
from .forms import AprendizForm

def lista_aprendices(request):
    aprendices = Aprendiz.objects.all()
    contexto = {'aprendices': aprendices} 
    return render(request, 'prueba/index.html', contexto)

def crear_aprendiz(request):
    form = AprendizForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Aprendiz fue creado correctamente')
        return redirect('listar_aprendices')
    
    return render(request, 'prueba/crear_aprendiz.html', {'form': form})

def editar_aprendiz(request, documento):
    aprendiz = get_object_or_404(Aprendiz, documento=documento)

    if request.method == 'POST':
        form = AprendizForm(request.POST, instance=aprendiz)
        form.fields['documento'].disabled = True
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado de manera correcta')
            return redirect('listar_aprendices')
    else:
        form = AprendizForm(instance=aprendiz)
        form.fields['documento'].disabled = True

    return render(request, 'prueba/formulario.html', {
        'form': form,
        'titulo': f'Editar {aprendiz.nombre} - {aprendiz.apellido}',
        'aprendiz': aprendiz
    })

def eliminar_aprendiz(request, documento):
    aprendiz = get_object_or_404(Aprendiz, documento=documento)

    if request.method == 'POST':
        aprendiz.delete()
        messages.success(request, 'Se eliminó el usuario correctamente')
        return redirect('listar_aprendices')

    return render(request, 'prueba/eliminar.html', {'aprendiz': aprendiz})