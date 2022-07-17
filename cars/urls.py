from django.urls import path
from cars.views import cars_response

urlpatterns = [
    path('all/', cars_response),
]

