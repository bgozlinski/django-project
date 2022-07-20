from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cars
from .forms import CarForm


def cars_response(request):
    all_cars = Cars.objects.all()  # ORM - Object Relational Mapping
    return render(request, 'cars.html', {'cars': all_cars,
                                         'range': range(len(all_cars) + 1)})


# CREATE
@login_required()
def cars_add(request):
    form = CarForm(request.POST or None, request.FILES or None)

    # jesli forma spelnia wymagania -> save()
    if form.is_valid():
        form.save()
        return redirect(cars_response)

    return render(request, 'car_form.html', {'form': form})


# UPDATE
@login_required()
def cars_edit(request, id):
    #  sprawdz czy obiekt istnieje pod id
    car = get_object_or_404(Cars, pk=id)

    form = CarForm(request.POST or None, request.FILES or None, instance=car)

    # jesli forma spelnia wymagania -> save()
    if form.is_valid():
        form.save()
        return redirect(cars_response)

    return render(request, 'car_form.html', {'form': form})


# DELETE
@login_required()
def cars_del(request, id):
    car = get_object_or_404(Cars, pk=id)

    if request.method == 'POST':
        car.delete()
        return redirect(cars_response)

    return render(request, 'accept_del.html', {'car': car})

