from django.http import HttpResponse, HttpResponseRedirect
from jmdr_crowfunding_app.forms import DonationForm, SupportForm
from jmdr_crowfunding_app.models import Donation, Support
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'jmdr_crowfunding/HTML/index.html')

def campanas(request):
    if request.method == 'GET':
        form = SupportForm()
        total = len(Support.objects.all())
        data = {'form': form, 'supporters_total': total}
    return render(request, 'jmdr_crowfunding/HTML/campanas.html', data)
    
def quienes_somos(request):
    return render(request, 'jmdr_crowfunding/HTML/quienes_somos.html')

def como_funciona(request):
    return render(request, 'jmdr_crowfunding/HTML/como_funciona.html')

def contacto(request):
    return render(request, 'jmdr_crowfunding/HTML/contacto.html')

def entrega_alimentos(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/entrega_alimentos/')
    else:
        form = DonationForm()
        data = {
            'donations': [
                {
                    'donor': donation.donor,
                    'amount': donation.amount,
                    'date_time': donation.date_time
                } for donation in Donation.objects.all()
            ],
            'form': form
        }
    return render(request, 'jmdr_crowfunding/HTML/entrega_alimentos.html', data)

def agregar_soporte(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/campanas/')
    # else:
    #     form = SupportForm()
    #     data = 

def asistencia_medica(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/asistencia_medica/')
    else:
        form = DonationForm()
        data = {
            'donations': [
                {
                    'donor': donation.donor,
                    'amount': donation.amount,
                    'date_time': donation.date_time
                } for donation in Donation.objects.all()
            ],
            'form': form
        }
    return render(request, 'jmdr_crowfunding/HTML/asistencia_medica.html', data)

def educacion(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/educacion/')
    else:
        form = DonationForm()
        data = {
            'donations': [
                {
                    'donor': donation.donor,
                    'amount': donation.amount,
                    'date_time': donation.date_time
                } for donation in Donation.objects.all()
            ],
            'form': form
        }
    return render(request, 'jmdr_crowfunding/HTML/educacion.html', data)