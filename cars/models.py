from django.db import models

class Cars(models.Model):
    marka = models.CharField(max_length=32, blank=False, default='')
    model = models.CharField(max_length=32, blank=False, default='')
    nr_wewnetrzny = models.PositiveSmallIntegerField(null=True, blank=True)
    rok_produkcji = models.PositiveSmallIntegerField(default=1970)
    data_przegladu_technicznego = models.DateField(null=True, blank=True)
    data_przegladu_serwisowego = models.DateField(null=True, blank=True)

    przebieg = models.PositiveIntegerField(default=0)

    opis = models.TextField(default='', blank=True)

    rodzaj_silnika_choices = [
        ('PB', 'Benzyna'),
        ('ON', 'Diesel'),
        ('Ele', 'Elektryczny'),
        ('Hybr', 'Hybrydowy'),
        (' ', ' ')
    ]

    rodzaj_silnika = models.CharField(max_length=4,
                                      choices=rodzaj_silnika_choices,
                                      default='')


    def __str__(self):
        return f'{self.marka} {self.model}'



