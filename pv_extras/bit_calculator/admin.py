from django.contrib import admin
from .models import UploadedFiles, GeneratedFiles


admin.site.register(UploadedFiles)
admin.site.register(GeneratedFiles)