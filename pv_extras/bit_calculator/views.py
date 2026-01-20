from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.conf import settings
from .forms import CSVFileUploadForm, BitRewardsFormSet
import logging
import os
from .src.file_validator import FileValidator
from .models import UploadedFiles, GeneratedFiles, CRN

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
        form = CSVFileUploadForm(request.POST, request.FILES, prefix='main_form')
        bit_rewards_formset = BitRewardsFormSet(request.POST, prefix="bit_rewards_formset")

        logger.info(request.POST)

        if form.is_valid() and bit_rewards_formset.is_valid():
            logger.info('form valid, can do stuff now')
        
            # check if CRN exists, if it doesn't, add to database
            try:
                CRN.objects.get(pk=form.cleaned_data['crn'])
            except CRN.DoesNotExist:
                newCRN = CRN(crn=int(form.cleaned_data['crn']))
                newCRN.save()

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
                    newForm = CSVFileUploadForm()
                    return render(request, "index.html", {'form': newForm, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'Invalid File Type (CSV Only)'})
                
                if not _FileValidator.isCSVFile(content):
                    newForm = CSVFileUploadForm()
                    return render(request, "index.html", {'form': newForm, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'Invalid File Type (CSV Only)'})
                
                uploadedFile = UploadedFiles(crn=int(form.cleaned_data['crn']), input_file=file, processed=True)
                
                # TODO: do processing and output file
                
                uploadedFile.save()
                
                newForm = CSVFileUploadForm()
                bit_rewards_formset = BitRewardsFormSet(prefix="bit_rewards_formset")
                return render(request, "index.html", {'form': newForm, 'bit_rewards': bit_rewards_formset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': False})
            else:
                newForm = CSVFileUploadForm()
                bit_rewards_formset = BitRewardsFormSet(prefix="bit_rewards_formset")
                return render(request, "index.html", {'form': newForm, 'bit_rewards': bit_rewards_formset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'File Too Large (' + f'{file.size}' + ' B)'})
        else:
            logger.info('form invalid')
            newForm = CSVFileUploadForm(prefix='main_form')
            bit_rewards_formset = BitRewardsFormSet(prefix="bit_rewards_formset")
            return render(request, "index.html", {'form': newForm, 'bit_rewards': bit_rewards_formset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'Invalid File'})

    newForm = CSVFileUploadForm(prefix='main_form')
    bit_rewards_formset = BitRewardsFormSet(prefix="bit_rewards_formset")
    return render(request, "index.html", {'form': newForm, 'bit_rewards': bit_rewards_formset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': False})

def download_uploaded_file(request):
    if request.method == "POST":
        try:
            fileToDownload = UploadedFiles.objects.filter(crn=request.POST.get('crn')).filter(input_file=request.POST.get('input_file_name'))
            logger.info(fileToDownload)
            return FileResponse(open(os.path.join(settings.MEDIA_ROOT, request.POST.get('input_file_name')), 'rb'), as_attachment=True)
        except:
            return redirect('index')

    return redirect('index')

def remove_uploaded_file(request):
    if request.method == "POST":
        try:
            row = UploadedFiles.objects.filter(crn=request.POST.get('crn')).filter(input_file=request.POST.get('input_file_name'))
            row.delete()

            return redirect('index')
        except:
            return redirect('index')
            
    return redirect('index')
