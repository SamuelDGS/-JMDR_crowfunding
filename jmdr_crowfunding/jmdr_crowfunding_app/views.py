from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'jmdr_crowfunding/html/index.html')

def campanas(request):
    return render(request, 'jmdr_crowfunding/html/campanas.html')