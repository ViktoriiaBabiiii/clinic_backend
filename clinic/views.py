from django.shortcuts import render, redirect
from django.http import HttpResponse
from clinic.models import Doctor, Appointment, Service
from rest_framework import viewsets
from clinic.models import Doctor, Service
from clinic.serializers import DoctorSerializer
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.http import HttpResponse
from clinic.forms.forms import AppointmentForm
from clinic.models import Appointment
from clinic.serializers import DoctorSerializer, AppointmentSerializer
from rest_framework import generics

class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentCreate(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


def service_list_api(request):
    services = list(Service.objects.values())
    return JsonResponse({'services': services}, safe=False)


def home(request):
    """ Render the homepage with a link to book an appointment. """
    return render(request, 'home.html')


def book_appointment(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        patient_first_name = request.POST.get('patient_first_name')
        patient_last_name = request.POST.get('patient_last_name')
        patient_email = request.POST.get('patient_email')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        comments = request.POST.get('comments')

        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            # Handle the case where the doctor does not exist
            return HttpResponse("Error: Doctor not found.", status=404)

        appointment = Appointment(
            patient_first_name=patient_first_name,
            patient_last_name=patient_last_name,
            patient_email=patient_email,
            doctor=doctor,
            appointment_date=appointment_date,
            comments=comments
        )
        appointment.save()
        return redirect('home')
    return render(request, 'book_appointment.html', {'doctors': doctors})


def service_list(request):
    """ View to display a list of services and their prices. """
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def doctor_list(request):
    """API view to display a list of doctors and their specializations in JSON format."""
    doctors = Doctor.objects.all()
    data = [{'first_name': doctor.first_name, 'last_name': doctor.last_name, 'specialization': doctor.specialization} for doctor in doctors]
    return JsonResponse({'doctors': data})



