"""
URL configuration for web_labs1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clinic.views import service_list_api, book_appointment, doctor_list, home, service_list
from clinic.views import DoctorList, AppointmentCreate  # Correctly import the views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('services/', service_list, name='services'),
    path('api/services/', service_list_api, name='api-services'),
    path('api/doctors/', DoctorList.as_view(), name='doctor-list'),
    path('api/appointments/', AppointmentCreate.as_view(), name='appointment-create'),
]
