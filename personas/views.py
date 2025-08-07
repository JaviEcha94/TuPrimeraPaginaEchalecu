from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
from django.db.models import Q

def listado_personas(request):
    query = request.GET.get("buscar")
    personas = Persona.objects.filter(Q(nombre__icontains=query) | Q(email__icontains=query)) if query else Persona.objects.all()
    return render(request, 'listado.html', {'personas': personas})

def agregar_persona(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listado')
    return render(request, 'formulario.html', {'form': form})
