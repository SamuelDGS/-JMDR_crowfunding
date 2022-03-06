from cProfile import label
from jmdr_crowfunding_app.models import Donation
from django import forms


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor', 'amount']
    # donor = forms.CharField(label='Nombre del donante', max_length=32)
    # amount = forms.FloatField(label='Monto')
    # currency = forms.ChoiceField(choices=['USD', 'BSV', 'EUR'])
