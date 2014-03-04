from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.models import urlresolvers
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from models import Submission, Comment
from forms import SubmissionForm

# Create your views here.

def submission_list(request):
	context = {}
	if request.method == 'GET':
		list = Submission.objects.all()
		context['submissions'] = list

	return render_to_response('submission-list.html', context, context_instance = RequestContext(request))

@login_required
def submit_submission(request):
	context = {}
	if request.method == 'POST':
		submission_form = SubmissionForm(request.POST, request.FILES)
		if submission_form.is_valid():
			submission = submission_form.save()
			context['submission_form'] = SubmissionForm()
			submission_id = submission.id
			return redirect('/submission')
		else:
			print 'Here'
			context['submission_form'] = submission_form
	else:
		context['submission_form'] = SubmissionForm()

	return render_to_response('create-submission.html', context, context_instance = RequestContext(request))

# class SubmissionView(DetailView):
# 	model = Submission
# 	template_name = 'submission.html'

# class ListSubmissionView(ListView):
# 	model = Submission
# 	template_name = 'submission_list.html'

# class CreateSubmissionView(CreateView):
# 	model = Submission,
# 	template_name = 'edit_submission.html'
# 	form_class = forms.SubmissionForm

# 	def get_success_url(self):
# 		return reverse('submission-list')

# 	def get_context_data(self, **kwargs):
# 		context = super(CreateSubmissionView, self).get_context_data(**kwargs)
# 		context['action'] = reverse('submission-new')

# 		return context

# class UpdateSubmissionView(UpdateView):
# 	model = Submission
# 	template_name = 'edit_submission.html'
# 	form_class = forms.SubmissionForm

# 	def get_success_url(self):
# 		return reverse('submission-list')

# 	def get_context_data(self, **kwargs):
# 		context = super(UpdateSubmissionView, self).get_context_data(**kwargs)
# 		context['action'] = reverse('submission-edit', 
# 			kwargs={'pk': self.get_object().id})

# 		return context

# class DeleteSubmissionView(DeleteView):
# 	model = Submission
# 	template_name = 'delete_submission.html'

# 	def get_success_url(self):
# 		return reverse('submission-list')