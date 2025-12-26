from django.shortcuts import render, HttpResponse
from .models import LabSection

# Create your views here.
def index(request):
    return render(request, "index.html", {'courses': LabSection.objects.all()})

def csv(request):
    return render(request, "csv.html")