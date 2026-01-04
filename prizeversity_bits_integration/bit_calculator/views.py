from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CSVFileUploadForm
import logging

logger = logging.getLogger(__name__)

# from .models import LabSection

# Create your views here.
def index(request):
    form = CSVFileUploadForm()
    return render(request, "index.html", {'form': form}) # {'courses': LabSection.objects.all()})

def csv(request):
    return render(request, "csv.html")

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def newCSVUpload(request):
    if request.method == 'POST':
        logger.info('POST method detected')
        form = CSVFileUploadForm(request.POST, request.FILES)
        logger.info('form created')
        if form.is_valid():
            logger.info('form valid, can do stuff now')

            return HttpResponseRedirect('')
        else:
            logger.info('form invalid')

    return HttpResponse('test')