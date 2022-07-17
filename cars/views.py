from django.shortcuts import render



def cars_response(request):
    return render(request, 'cars.html')
