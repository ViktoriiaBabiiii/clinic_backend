from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.specialization})"


class Appointment(models.Model):
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    patient_email = models.EmailField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return (f"Appointment for {self.patient_first_name} {self.patient_last_name} "
                f"with Dr. {self.doctor.first_name} {self.doctor.last_name} "
                f"on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}")


class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
