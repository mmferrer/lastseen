from django.conf.urls import patterns, include, url
# <<<<<<< HEAD
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# =======
from accounts.views import *
from submissions.views import *
# >>>>>>> 36f0cd79ad43c4f33931978cb4ae3062c9198619
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^/', include('homepage.urls')),
	# url(r'^accounts/', include('accounts.urls')),
	url(r'^admin/', include(admin.site.urls)),

	url(r'^submission/all', 'submissions.views.view_all'),
	url(r'^submission/(\d+)/$', 'submissions.views.view'),
	url(r'^submission/add/', add),
	url(r'^submission/edit/(\d+)/$', 'submissions.views.edit'),
	url(r'^submission/delete/(\d+)/$','submissions.views.delete'),

	url(r'^submission/(\d+)/comment/$', 'comments.views.add'),
	url(r'^submission/(\d+)/comment/all$', 'comments.views.view_all'),

	url(r'^signup/', signup),
	url(r'^accounts/profile/$', profile),
	url(r'^profile/(\d+)/$',singleprofile),
	url(r'^list/',accountList),
    url(r'^logout/',logout_view),
    url(r'^accounts/login/$',
        user_login, name = 'login'),
   url(r'^login/$', user_login),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# <<<<<<< HEAD
# =======
# 	url(r'^admin/', include(admin.site.urls)),
# 	url(r'^signup/', signup),
# 	url(r'^account/profile$',profile, name= 'profilepage'),
# 	url(r'^profile/(\d+)/$',singleprofile),
# 	url(r'^list/',accountList),
# )
# >>>>>>> 36f0cd79ad43c4f33931978cb4ae3062c9198619
