# Generated by Django 4.0.5 on 2022-07-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_model_cars_rodzaj_silnika_cars_rok_produkcji_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='data_przegladu_serwisowego',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='data_przegladu_technicznego',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='opis',
            field=models.TextField(default=''),
        ),
    ]
