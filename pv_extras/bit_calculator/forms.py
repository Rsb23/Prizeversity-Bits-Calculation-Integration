from django import forms
from django.core.validators import FileExtensionValidator

class CSVFileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput, validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    crn = forms.IntegerField(widget=forms.NumberInput)
    bitRewards = forms.CharField(widget=forms.TextInput)
    firstNSubmissionBonus = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    n = forms.IntegerField(widget=forms.NumberInput)
    submissionStreak = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    streakWeeks = forms.CharField(widget=forms.TextInput)
    dualCompletion = forms.BooleanField(required=False, widget=forms.CheckboxInput)