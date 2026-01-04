from django import forms


class CSVFileUploadForm(forms.Form):
    # obj attrs are daisyUI + Tailwind CSS styling
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'file-input file-input-bordered w-full max-w-xs'
    }))
    crn = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'input input-bordered w-full max-w-xs',
        'placeholder': 'Enter CRN'
    }))
    bitRewards = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input-bordered w-full max-w-xs',
        'placeholder': 'Bit rewards'
    }))
    firstNSubmissionBonus = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'checkbox'
    }))
    n = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'input input-bordered w-full max-w-xs'
    }))
    submissionStreak = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'checkbox'
    }))
    streakWeeks = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input-bordered w-full max-w-xs'
    }))
    dualCompletion = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'checkbox'
    }))