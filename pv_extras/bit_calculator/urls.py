from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('csv/', views.csv, name='csv'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('download-uploaded-file/', views.download_uploaded_file, name='download_uploaded_file'),
    path('remove-uploaded-file/', views.remove_uploaded_file, name='remove_uploaded_file'),
]