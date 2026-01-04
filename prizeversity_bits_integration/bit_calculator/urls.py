from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("csv/", views.csv, name="csv"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    path('new-csv-upload/', views.newCSVUpload, name="newCSVUpload")
]