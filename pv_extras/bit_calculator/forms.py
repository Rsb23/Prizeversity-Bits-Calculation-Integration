from django import forms
from django.forms import formset_factory
from django.core.validators import FileExtensionValidator

class CSVFileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput, validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    crn = forms.IntegerField(widget=forms.NumberInput)
    # bitRewards field has a dynamic size and will therefore be represented and rendered with a django formset
    firstNSubmissionBonus = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    n = forms.IntegerField(required=False, widget=forms.NumberInput)
    submissionStreak = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    streakWeeks = forms.CharField(required=False, widget=forms.TextInput)
    dualCompletion = forms.BooleanField(required=False, widget=forms.CheckboxInput)

class BitRewards(forms.Form):
    bitRewards = forms.CharField()

# TODO: move to views.py when completed and reading DB for config
BitRewardsFormSet = formset_factory(
    BitRewards,
    extra=0,  # initial amount, 
    max_num=20,  # max is the amount of weeks in the semester (20 in this case), get from DB when config saving works
    can_delete=True
)
