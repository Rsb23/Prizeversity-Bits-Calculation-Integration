from django.shortcuts import render, HttpResponse
# from .models import TodoItem

# Create your views here.
def index(request):
    return render(request, "index.html")

def csv(request):
    return render(request, "csv.html")