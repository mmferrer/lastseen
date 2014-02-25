from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def signup(request, template_name='accounts/signup.html', 
    email_template_name='accounts/signup_email.html',
    signup_form=UserCreationForm):

    context = {}
    if request.method == "POST":
        requestform = signup_form(request.POST,request.FILES)
        if requestform.is_valid():
            requestform.save()
            opts = {}
            opts['use_https'] = request.is_secure()
            opts['email_template_name'] = email_template_name
            user = authenticate(username=requestform.cleaned_data['username'], password=requestform.cleaned_data['password'])
            loginaccount(request, user)
            return HttpResponseRedirect('/welcome')
    else:
       requestform = signup_form()

    return render_to_response(template_name, {'register_form': requestform,}, context_instance=RequestContext(request))
