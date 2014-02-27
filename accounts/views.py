from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from accounts.forms import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
# Create your views here.
@csrf_protect
def signup(request):
    context = {}
    if request.method == "POST":
        requestform = UserCreationForm(request.POST,request.FILES)
        if requestform.is_valid():
            obj = requestform.save()
            context['register_form'] = UserCreationForm()
            #user = authenticate(username=requestform.cleaned_data['username'], password=requestform.cleaned_data['password'])
            #loginaccount(request, user)
            userId = obj.id
            return redirect('/profile/%d' % userId)
        else:
            print ' ERROR !'
            context['register_form']= requestform
         #  requestform = signup_form()
    else:
        context['register_form']= UserCreationForm()

    return render_to_response("signup_form.html",context, context_instance=RequestContext(request))

@login_required
def profile(request, form_id):
    context = {}
    if request.method == 'GET':
        print request.user
        myprofile = UserAccount.objects.all()
        context['list_view'] = myprofile

    return render_to_response('profile.html', context, context_instance=RequestContext(request))

def accountList(request):
    context = {}
    if request.method == 'GET':
        alist = UserAccount.objects.all()
        context['account_list'] = alist

    return render_to_response('accountlist.html',context,context_instance=RequestContext(request))

@login_required
def singleprofile(request, form_id):
    context = {}
    if request.method == 'GET':
        print request.user
        myprofile = UserAccount.objects.all().filter(id = form_id)
        context['list_view'] = myprofile

    return render_to_response('profile.html', context, context_instance=RequestContext(request))