from django import forms
from clinic.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_first_name', 'patient_last_name', 'patient_email', 'doctor', 'appointment_date', 'comments']
