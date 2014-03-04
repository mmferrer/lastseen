from django import forms
from submissions.models import *
from django.forms import ModelForm

class AddSubmission(forms.ModelForm):

	class Meta:
		model = Submission
		exclude = ['author', 'date', 'time', 'found', 'longitude', 'latitude', 'lasttime', 'lastdate']
		widgets = {
			'title': forms.TextInput(attrs={ 'placeholder': 'Title' }),
			'details': forms.Textarea(attrs={ 'placeholder': 'Details'}),
		}

class EditSubmission(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(EditSubmission, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		print instance.found
		print str(instance.latitude)
		if instance and instance.pk:
			self.fields['author'].widget.attrs['readonly'] = True

	class Meta:
		model = Submission
		exclude = ['date', 'time', 'lasttime', 'lastdate']
		widgets = {
			'title': forms.TextInput(attrs={ 'placeholder': 'Title' }),
			'details': forms.Textarea(attrs={ 'placeholder': 'Details'}),
			'found': forms.RadioSelect(),
		}