from django.conf.urls.defaults import *
from accounts.views import *

urlpatterns = patterns('accounts.views',
    url(r'^(?P<id>\d+)/(?P<slug>[-\w\d]+)/$',view=profile, name='profile'),    
)

'''
urlpatterns = patterns('',
		(r'^signup/$'
			'lastseen.accounts.views.signup',
			{'template_name':'accounts/signup_form.html'})

		



		)
'''

j