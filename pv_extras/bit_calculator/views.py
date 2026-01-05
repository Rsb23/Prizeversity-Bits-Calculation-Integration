from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CSVFileUploadForm
import logging
from .src.file_validator import FileValidator
from .models import UploadedFiles, GeneratedFiles

logger = logging.getLogger(__name__)


# Create your views here.
def csv(request):
    return render(request, "csv.html")

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def index(request):
    if request.method == 'POST':
        form = CSVFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info('form valid, can do stuff now')

            # we already checked uploaded file extension with
            # filter (in file dialog, HTML accept attr)
            # and check filename extension (Django FileExtensionValidator)
            # still need to validate actual file content because extension
            # because extension can be changed and is a SECURITY RISK

            logger.info('started file validation')

            _FileValidator = FileValidator()
            file = form.cleaned_data['file']

            content = file.read()
            file_content_type = file.content_type

            if file.size < 4096:  # change max size based on PROD memory avaiable and max onlinegdb expected file size
                if file_content_type != 'text/csv' and file_content_type != 'application/csv':
                    return HttpResponse('INVALID CSV')
                
                if not _FileValidator.isCSVFile(content):
                    return HttpResponse('INVALID CSV')
                
                uploadedFile = UploadedFiles(crn=int(form.cleaned_data['crn']), input_file=file, processed=True)
                
                # TODO: do processing and output file
                
                uploadedFile.save()
                
                newForm = CSVFileUploadForm()
                return render(request, "index.html", {'form': newForm})
            else:
                return HttpResponse('INVALID CSV, FILE TOO LARGE (' + f'{file.size}' + ' B)')
        else:
            logger.info('form invalid')

    form = CSVFileUploadForm()
    return render(request, "index.html", {'form': form})

