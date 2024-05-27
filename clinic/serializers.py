# serializers.py
from clinic.models import Doctor
from datetime import time  # Add this import
from rest_framework import serializers
from clinic.models import Doctor, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialization']

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['patient_first_name', 'patient_last_name', 'patient_email', 'doctor', 'appointment_date', 'comments']


    def validate_appointment_date(self, value):
        if value.time() < time(8, 0) or value.time() > time(18, 0):
            raise serializers.ValidationError("Appointments can only be booked between 08:00 and 18:00.")
        return value

