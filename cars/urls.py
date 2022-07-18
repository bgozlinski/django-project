from django.urls import path
from cars.views import cars_response, cars_add, cars_edit, cars_del



urlpatterns = [
    path('all/', cars_response),
    path('add/', cars_add),
    path('edit/<int:id>', cars_edit),
    path('del/<int:id>', cars_del),
]

