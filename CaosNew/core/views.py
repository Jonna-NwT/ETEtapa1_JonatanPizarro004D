from django.shortcuts import render, redirect
from .models import Colaborador# Create ----------------------------------------------------------------------------------
from .forms import RegisterColaborador# Create ----------------------------------------------------------------------------------
# Create your views here.
def index(request):
    return render(request, 'index.html')

def crearColaborador(request):# Create ----------------------------------------------------------------------------------
    if request.method == 'POST':      
        form_colaboradores = RegisterColaborador(request.POST, files=request.FILES) #CAMBIE ALGO
        if form_colaboradores.is_valid():
            form_colaboradores.save()
            return redirect('index')
    else:
        form_colaboradores = RegisterColaborador()
    return render(request, 'core/registrar_colaboradores.html', {'form_colaboradores' : form_colaboradores})