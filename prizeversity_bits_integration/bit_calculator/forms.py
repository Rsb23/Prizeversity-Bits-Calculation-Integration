from django import forms


class CSVFileUploadForm(forms.Form):
    file = forms.FileField()
    crn = forms.IntegerField()
    bitRewards = forms.CharField()
    firstNSubmissionBonus = forms.BooleanField()
    n = forms.IntegerField()
    submissionStreak = forms.BooleanField()
    streakWeeks = forms.CharField()
    dualCompletion = forms.BooleanField()