from django.db import models

# Create your models here.
class LabSections(models.Model):
    csv_input_file = models.FileField()
    upload_date = models.DateTimeField()
    crn = models.IntegerField()

class Rewards(models.Model):
    bit_rewards = models.CharField()
    week = models.IntegerField()
    crn = models.IntegerField()
    last_updated = models.DateTimeField()

"""
    LabSections

    id crn input_csv             upload_datetime  processed 
    ------------------------------------------------------------
    1  101 test.csv              12-29-2025       true
    2  101 another_file.csv      12-29-2025       false

    compositekey

    GeneratedCSVs
    
    id crn output_csv            output_datetime
    --------------------------------------------
    1  101 test_output.csv              12-29-2025
    2  101 another_file_output.csv      12-29-2025


    select file from labsections where crn = ?1;
"""