from django.forms import ModelForm
from .models import Cars


class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields =['nr_wewnetrzny',
                 'data_przegladu_technicznego',
                 'data_przegladu_serwisowego',
                 'przebieg',
                 'rodzaj_silnika',
                 'opis',
        ]