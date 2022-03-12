"""jmdr_crowfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jmdr_crowfunding_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('campanas/', views.campanas, name='campanas'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('como_funciona/', views.como_funciona, name='como_funciona'),
    path('contacto/', views.contacto, name='contacto'),
    path('entrega_alimentos/', views.entrega_alimentos, name='entrega_alimentos'),
    path('asistencia_medica/', views.asistencia_medica, name='asistencia_medica'),
    path('educacion/', views.educacion, name='educacion'),
    path('agregar_soporte/', views.agregar_soporte, name='agregar_soporte'),
]
