from cProfile import label
from jmdr_crowfunding_app.models import Donation, Support
from django import forms
from django.db import models


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor', 'amount']
    donor = forms.CharField(label='Nombre del donante', max_length=32)
    amount = forms.FloatField(label='Monto')

class SupportForm(forms.ModelForm):
    class Department(models.TextChoices):
        ALIMENTOS = 'ALIM'
        ASIS_MEDICA = 'ASIS_MED'
        EDUC = 'EDUC'

    class Meta:
        model = Support
        fields = ['name', 'last_name', 'email', 'phone_number', 'department']

    name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Teléfono')
    department = forms.ChoiceField(label='Departamento', choices=Department.choices)
