import uuid
from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    start_date = models.DateTimeField(default=timezone.now, db_column='start_date')
    end_date = models.DateTimeField(db_column='end_date', null=True)
    price = models.DecimalField(default=200, max_digits=10, decimal_places=2, db_column="price")

    patient = models.ForeignKey("Patient", related_name="Appointments", db_column="patient_id", on_delete=models.PROTECT)
    physician = models.ForeignKey("Physician", related_name="Appointments", db_column="physician_id", on_delete=models.PROTECT)

    class Meta:
        db_table = "appointment"
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    name = models.CharField(max_length=150, db_column='name')

    class Meta:
        db_table = "patient"
        verbose_name = "Patient"
        verbose_name_plural = "Patients"


class Physician(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    name = models.CharField(max_length=150, db_column='name')

    class Meta:
        db_table = "physician"
        verbose_name = "Physician"
        verbose_name_plural = "Physicians"


class Charge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    value = models.DecimalField(default=200, max_digits=10, decimal_places=2, db_column="value")

    appointment = models.ForeignKey("Appointment", related_name="Charges", db_column="appointment_id", on_delete=models.PROTECT)

    class Meta:
        db_table = "charge"
        verbose_name = "Charge"
        verbose_name_plural = "Charges"
