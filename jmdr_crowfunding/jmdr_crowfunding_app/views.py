from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'jmdr_crowfunding/HTML/index.html')

def campanas(request):
    return render(request, 'jmdr_crowfunding/HTML/campanas.html')
    
def quienes_somos(request):
    return render(request, 'jmdr_crowfunding/HTML/quienes_somos.html')

def como_funciona(request):
    return render(request, 'jmdr_crowfunding/HTML/como_funciona.html')

def contacto(request):
    return render(request, 'jmdr_crowfunding/HTML/contacto.html')

def entrega_alimentos(request):
    return render(request, 'jmdr_crowfunding/HTML/entrega_alimentos.html')

def asistencia_medica(request):
    return render(request, 'jmdr_crowfunding/HTML/asistencia_medica.html')

def educacion(request):
    return render(request, 'jmdr_crowfunding/HTML/educacion.html')