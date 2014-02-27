from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse

from models import Submission, Comment

# Create your views here.
class SubmissionView(DetailView):
	model = Submission
	template_name = 'submission.html'

class ListSubmissionView(ListView):
	model = Submission
	template_name = 'submission_list.html'

class CreateSubmissionView(CreateView):
	model = Submission,
	template_name = 'edit_submission.html'

	def get_success_url(self):
		return reverse('submission-list')

	def get_context_data(self, **kwargs):
		context = super(CreateSubmissionView, self).get_context_data(**kwargs)
		context['action'] = reverse('submission-new')

		return context

class UpdateSubmissionView(UpdateView):
	model = Submission
	template_name = 'edit_submission.html'

	def get_success_url(self):
		return reverse('submission-list')

	def get_context_data(self, **kwargs):
		context = super(UpdateSubmissionView, self).get_context_data(**kwargs)
		context['action'] = reverse('submission-edit', 
			kwargs={'pk': self.get_object().id})

		return context

class DeleteSubmissionView(DeleteView):
	model = Submission
	template_name = 'delete_submission.html'

	def get_success_url(self):
		return reverse('submission-list')