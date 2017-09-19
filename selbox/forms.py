from django import forms
from .models import *

class SBForm(forms.Form):
    def __init__(self, run_choices, *args, **kwargs):
        super(SBForm, self).__init__(*args, **kwargs)
        self.fields["run_hist"] = forms.ChoiceField(label='Select Run', choices=run_choices)

class ModCForm(forms.Form):
    run_hist = forms.ModelChoiceField(queryset=RunHistory.objects.all(), to_field_name="id")
    
