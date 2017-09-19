from django import forms

class SBForm(forms.Form):
	run_hist = forms.ChoiceField(label='Select Run')
	run_hist.choices = (('1', 'Just me'),)
