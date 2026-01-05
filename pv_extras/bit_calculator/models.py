from django.db import models

class UploadedFiles(models.Model):
    crn = models.IntegerField()
    input_file = models.FileField()
    upload_date = models.DateField(auto_now_add=True)
    upload_time = models.TimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.input_file.name

class GeneratedFiles(models.Model):
    crn = models.IntegerField()
    output_file = models.FileField()
    upload_date = models.DateField(auto_now_add=True)
    upload_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.input_file.name