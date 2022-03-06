from django.db import models

# Create your models here.
class Donation(models.Model):
    class Department(models.TextChoices):
        ALIMENTOS = 'ALIM'
        ASIS_MEDICA = 'ASIS_MED'
        EDUC = 'EDUC'

    donor = models.CharField(max_length=32)
    amount = models.FloatField()
    currency = models.CharField(max_length=3)
    date_time = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=12, choices=Department.choices)
