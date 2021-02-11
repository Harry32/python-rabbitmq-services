import uuid
from django.db import models


class Charge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    value = models.DecimalField(default=200, max_digits=10, decimal_places=2, db_column="value")

    appointment = models.UUIDField(editable=False, db_column='appointment_id')

    class Meta:
        managed = False

        db_table = "charge"
        verbose_name = "Charge"
        verbose_name_plural = "Charges"
