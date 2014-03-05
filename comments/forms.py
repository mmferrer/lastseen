from django import forms
from comments.models import *
from django.forms import ModelForm

class AddComment(forms.ModelForm):

	class Meta:
		model = Comment
		exclude = ['submission', 'user', 'author', 'date', 'time', 'longitude', 'latitude', 'lasttime', 'lastdate']
		widgets = {
			'title': forms.TextInput(attrs={ 'placeholder': 'Title' }),
			'details': forms.Textarea(attrs={ 'placeholder': 'Details'}),
		}

class EditComment(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(EditComment, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		print instance.found
		if instance and instance.pk:
			self.fields['author'].widget.attrs['readonly'] = True

	class Meta:
		model = Comment
		exclude = ['date', 'time']
		widgets = {
			'title': forms.TextInput(attrs={ 'placeholder': 'Title' }),
			'details': forms.Textarea(attrs={ 'placeholder': 'Details'}),
		}