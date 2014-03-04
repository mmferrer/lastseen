from django import forms
from django.forms import ModelForm
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import int_to_base36
from django.template import Context, loader
from django.core.exceptions import ValidationError

from models import Submission, Comment
from accounts.models import UserAccount

class SubmissionForm(forms.ModelForm):

	class Meta:
		model = Submission

	# confirm_lat = forms.FloatField('Confirm latitude', required=True,)

	# class Meta:
	# 	model = Submission

	# def __init__(self, *args, **kwargs):
	# 	if kwargs.get('instance'):
	# 		latitude = kwargs['instance'].latitude
	# 		kwargs.setdefault('initial', {})['confirm_lat'] = latitude

	# 	return super(SubmissionForm, self).__init__(*args, **kwargs)

	# def clean(self):
	# 	if (self.cleaned_data.get('latitude') != self.cleaned_data.get('confirm_lat')):
	# 		raise ValidationError("Latitude does not match.")

	# 	return self.cleaned_data 