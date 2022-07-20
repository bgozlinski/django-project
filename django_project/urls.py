from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #  autoryzacja uzytkownika

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

