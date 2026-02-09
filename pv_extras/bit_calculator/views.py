from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.conf import settings
from .forms import CSVFileUploadForm, BitRewardsFormSet
import logging
import os
from .src.file_validator import FileValidator
from .src.csv_handling import DataHandler
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
    # TODO: create method to handle formset creation by checking databae for CRN config to bound form with previously saved values
    if request.method == 'POST':
        # bound both base form and formset for bit rewards widget
        form = CSVFileUploadForm(request.POST, request.FILES)
        bitRewardsFormset = BitRewardsFormSet(request.POST)

        logger.info(request.POST)  # just for debugging

        if form.is_valid() and bitRewardsFormset.is_valid():
            logger.info('form valid, can do stuff now')
        
            # check if CRN exists, if it doesn't, add to database
            try:
                CRN.objects.get(pk=form.cleaned_data['crn'])
            except CRN.DoesNotExist:
                newCRN = CRN(crn=int(form.cleaned_data['crn']))
                newCRN.save()

            for week in bitRewardsFormset:
                if week.cleaned_data and not week.cleaned_data.get("DELETE"):
                    pass
                    # TODO: save to config DB based on CRN here
                    # TODO: save to local list variable for passing to backend processing

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
                    newFormset = BitRewardsFormSet()
                    return render(request, "index.html", {'form': newForm, 'formset': newFormset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'Invalid File Type (CSV Only)'})
                
                if not _FileValidator.isCSVFile(content):
                    newForm = CSVFileUploadForm()
                    newFormset = BitRewardsFormSet()
                    return render(request, "index.html", {'form': newForm, 'formset': newFormset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'Invalid File Type (CSV Only)'})
                
                uploadedFile = UploadedFiles(crn=int(form.cleaned_data['crn']), input_file=file, processed=True)
                
                # TODO: do processing and output file
                # we first have to determine what criteria the user wants to be used to calculate
                
                # set initial values, one to one variables with the form prototype CSVFileUploadForm
                crn = -1  # course CRN number, used for saving config and getting past uploaded files, very important
                
                firstNSubmissionsBonus = False
                n = -1  # first 10 students to submit get this extra bit reward
                
                submissionStreak = False
                streakWeeks = -1  # bit reward amount to give to students for maintaining weekly streaks

                dualCompletion = False  # TODO: convert to int, 15 bits for testing, give students extra bits for completing both DD for that week

                # for testing only, this should be retrieved from weekly bit rewards dynamic widget
                weeklyBitRewards = [5] * 20

                # the first bool for the following conditionals represents the enable checkbox for each criteria, 
                # this is identical to the form prototype

                # set values from POST data
                crn = form.cleaned_data['crn']

                if (form.cleaned_data['firstNSubmissionBonus']):
                    firstNSubmissionsBonus = True
                    n = form.cleaned_data['n']
                
                if (form.cleaned_data['submissionStreak']):
                    submissionStreak = True
                    streakWeeks = form.cleaned_data['streakWeeks']
                
                if (form.cleaned_data['dualCompletion']):
                    dualCompletion = True

                # now we can start passing data to the backend to get an output file
                
                _datahandler = DataHandler(content, UploadedFiles.objects.filter(crn=crn).order_by('upload_date').latest('upload_time'), decodeFiles=False)

                # pass criteria to backend for abstracted handling only receiving output data
                _datahandler.createOutputFile(firstNSubmissionsBonus, n, submissionStreak, streakWeeks, dualCompletion)

                # convert output data to file

                # add file to GeneratedFiles
                
                
                uploadedFile.save()
            else:
                logger.info('file size too large')
                newForm = CSVFileUploadForm()
                newFormset = BitRewardsFormSet()
                return render(request, "index.html", {'form': newForm, 'formset': newFormset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'File Size Too Large'})
        else:
            logger.info('form invalid')
            newForm = CSVFileUploadForm()
            newFormset = BitRewardsFormSet()
            return render(request, "index.html", {'form': newForm, 'formset': newFormset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all(), 'file_error': True, 'file_error_msg': 'Invalid File Type (CSV Only)'})

    newForm = CSVFileUploadForm()
    newFormset = BitRewardsFormSet()
    return render(request, "index.html", {'form': newForm, 'formset': newFormset, 'crn_data': CRN.objects.all(), 'gen_files_data': GeneratedFiles.objects.all(), 'up_files_data': UploadedFiles.objects.all()})

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
