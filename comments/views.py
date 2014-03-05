from comments.forms import AddComment, EditComment
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from comments.models import Comment
from submissions.models import Submission
from accounts.models import UserAccount
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date, time

def add(request, form_id):
	context = {}
	if request.method == 'POST':
		comment_form = AddComment(request.POST, request.FILES)
		if comment_form.is_valid():
			submission = Submission.objects.get(id = form_id)

			comment = comment_form.save(commit = False)
			comment.submission = submission

			if request.user.id == None:
				print 'None'
				comment.author = 'Anonymous'
			else:
				user = UserAccount.objects.get(id = request.user.id)
				comment.user = user
				comment.author = user.username

			comment.lastdate = date.today()
			comment.lasttime = datetime.datetime.now()
			comment.date = date.today()
			comment.time = datetime.datetime.now()

			comment.address = request.POST['address']

			lat = request.POST['latitude']
			lng = request.POST['longitude']

			comment.latitude = float(lat)
			comment.longitude = float(lng)
			comment.save()

			context['comment'] = AddComment()
			context['comment_title'] = comment.title
			context['comment_details'] = comment.details
			# context['view_submission'] = '/submissions/%d' & submission.id
			# context['profile'] = '/profile/%s' & request.user.id

			return redirect('/submission/%d' % submission.id)
		else:
			print 'Invalid'
			context['comment'] = comment_form
	else:
		context['comment'] = AddComment()

	return render_to_response('create_comment.html', context, context_instance = RequestContext(request))

def view_all(request, form_id):
	context = {}
	if request.method == 'GET':
		submission = Submission.objects.get(id = form_id)
		comment_list = Comment.objects.all().filter(submission = submission).order_by('-date', '-time')
		context['comments'] = comment_list

	return render_to_response('comment_list.html', context, context_instance = RequestContext(request))

# from submissions.forms import AddSubmission, EditSubmission
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template.loader import get_template
# from django.template import RequestContext
# from django.template import Context
# from django.http import HttpResponse
# from django.shortcuts import render_to_response, redirect
# from submissions.models import Submission
# from accounts.models import UserAccount
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required
# import datetime
# from datetime import date, time

# # Create your views here.
# def add(request):
# 	context = {}
# 	if request.method == 'POST':
# 		submission_form = AddSubmission(request.POST, request.FILES)
# 		if submission_form.is_valid():
# 			submission = submission_form.save(commit = False)
# 			submission.author = request.user
# 			submission.date = date.today()
# 			submission.time = datetime.datetime.now()
# 			submission.found = False

# 			submission.address = request.POST['address']

# 			lat = request.POST['latitude']
# 			lng = request.POST['longitude']

# 			submission.latitude = float(lat)
# 			submission.longitude = float(lng)
# 			submission_form.save()

# 			print lat
# 			print lng

# 			context['add_submission'] = AddSubmission()
# 			context['submission_id'] = submission.id
# 			context['submission_title'] = submission.title
# 			context['submission_details'] = submission.details
# 			# context['view_submission'] = '/submissions/%d' & submission.id
# 			# context['profile'] = '/profile/%s' & request.user.id

# 			return redirect('/submission/%d' % submission.id)
# 		else:
# 			print 'Invalid'
# 			context['add_submission'] = submission_form
# 	else:
# 		context['add_submission'] = AddSubmission()

# 	return render_to_response('create_submission.html', context, context_instance = RequestContext(request))

# def view(request, form_id):
# 	context = {}
# 	submission = Submission.objects.get(id = form_id)
# 	if request.method == 'GET':
# 		context['submission'] = submission

# 	return render_to_response('submission.html', context, context_instance = RequestContext(request))

# def view_all(request):
# 	context = {}
# 	if request.method == 'GET':
# 		submission_list = Submission.objects.all().order_by('-date', '-time')
# 		context['submissions'] = submission_list

# 	return render_to_response('submission_list.html', context, context_instance = RequestContext(request))

# def edit(request, form_id):
# 	context = {}
# 	submission = Submission.objects.get(id=form_id)
# 	submission_form = EditSubmission(instance = submission)
# 	if request.method == 'POST':
# 		submission_form = EditSubmission(request.POST, request.FILES)
# 		if submission_form.is_valid():
# 			edited = submission_form.save(commit = False)
# 			edited.id = submission_form.id
# 			edited.author = submission_form.user.username
# 			edited.time = datetime.datetime.now()
# 			edited.date = date.today()
# 			submission_form.save()

# 			context['submission_id'] = submission.id

# 			return render_to_response('submission_success.html', context, context_instance = RequestContext(request))
# 	else:
# 		context['submission'] = submission_form
# 	return render_to_response('edit_submission.html', context, context_instance = RequestContext(request))

# def delete(request, form_id):
# 	context={}
# 	submission = Submission.objects.get(pk = form_id)
#    	submission.delete()
#    	return redirect('/submission/all')



