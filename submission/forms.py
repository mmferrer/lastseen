from django import forms
from django.core.exceptions import ValidationError

from models import Submission, Comment

class SubmissionForm(forms.ModelForm):

	confirm_lat = forms.FloatField('Confirm latitude', required=True,)

	class Meta:
		model = Submission

	def __init__(self, *args, **kwargs):
		if kwargs.get('instance'):
			latitude = kwargs['instance'].latitude
			kwargs.setdefault('initial', {})['confirm_lat'] = latitude

		return super(SubmissionForm, self).__init__(*args, **kwargs)

	def clean(self):
		if (self.cleaned_data.get('latitude') != self.cleaned_data.get('confirm_lat')):
			raise ValidationError("Latitude does not match.")

		return self.cleaned_data 