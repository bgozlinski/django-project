# Generated by Django 4.0.5 on 2022-07-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_cars_przebieg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='przebieg',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cars',
            name='rok_produkcji',
            field=models.PositiveSmallIntegerField(default=1970),
        ),
    ]
