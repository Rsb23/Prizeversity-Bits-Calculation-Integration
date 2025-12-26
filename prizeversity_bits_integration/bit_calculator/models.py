from django.db import models

# Create your models here.
class LabSection(models.Model):
    dateCreated = models.DateField()
    timeCreated = models.TimeField()
    crn = models.IntegerField()