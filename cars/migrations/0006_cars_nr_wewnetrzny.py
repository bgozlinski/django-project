# Generated by Django 4.0.5 on 2022-07-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_cars_przebieg_alter_cars_rok_produkcji'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='nr_wewnetrzny',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
