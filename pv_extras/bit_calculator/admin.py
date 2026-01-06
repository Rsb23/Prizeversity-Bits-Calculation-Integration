from django.contrib import admin
from .models import UploadedFiles, GeneratedFiles, CRN


admin.site.register(UploadedFiles)
admin.site.register(GeneratedFiles)
admin.site.register(CRN)