from django.shortcuts import render, redirect
from .models import Colaborador# Create ----------------------------------------------------------------------------------
from .forms import RegisterColaborador,formModificarColaborador# Create ----------------------------------------------------------------------------------
# Create your views here.

def index(request):
    return render(request, 'index.html')

def crearColaborador(request):# Create ----------------------------------------------------------------------------------
    if request.method == 'POST':      
        form_colaboradores = RegisterColaborador(request.POST, files=request.FILES) #CAMBIE ALGO
        if form_colaboradores.is_valid():
            #formacion de password con la informacion entregada
            newPass = (form_colaboradores.cleaned_data['rutColaborador'])[0:2] + ((form_colaboradores.cleaned_data['nombreCompleto'])[0:2]).upper() + ((form_colaboradores.cleaned_data['pais'])[-2:]).lower() + str(form_colaboradores.cleaned_data['telefono'])[-2:]
            rut = form_colaboradores.cleaned_data['rutColaborador']
            form_colaboradores.save()
            paswordNew = Colaborador.objects.get(rutColaborador=rut)
            paswordNew.contraseña = newPass
            paswordNew.save()
            return redirect('ver-todos')
    else:
        form_colaboradores = RegisterColaborador()
    return render(request, 'core/registrar_colaboradores.html', {'form_colaboradores' : form_colaboradores})
    
def verTodos(request):
    Colaboradores = Colaborador.objects.all()
    return render(request, 'core/vertodos.html', context={'colaboradores':Colaboradores})






















def modificarColaborador(request, id):
    colaborador = Colaborador.objects.get(rutColaborador=id)
    datos = {
        'form' : formModificarColaborador(instance=colaborador)
    }
    if request.method == 'POST':
        formulario = formModificarColaborador(data=request.POST, instance=colaborador, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect('ver-todos')
    return render(request, 'core/modificar_colaborador.html', datos)

def eliminarColaborador(request, id):
    colaborador = Colaborador.objects.get(rutColaborador=id)
    colaborador.delete()
    return redirect('ver-todos')