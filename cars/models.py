from django.db import models


class Cars(models.Model):
    nr_wewnetrzny = models.PositiveSmallIntegerField(null=True, blank=True)
    data_przegladu_technicznego = models.DateField(null=True, blank=True)
    data_przegladu_serwisowego = models.DateField(null=True, blank=True)
    przebieg = models.PositiveIntegerField(default=0)

    rodzaj_silnika_choices = [
        ('PB', 'Benzyna'),
        ('ON', 'Diesel'),
        ('Ele', 'Elektryczny'),
        ('Hybr', 'Hybryda'),
        (' ', ' ')
    ]

    rodzaj_silnika = models.CharField(max_length=4,
                                      choices=rodzaj_silnika_choices,
                                      default='')

    opis = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.nr_wewnetrzny}'
