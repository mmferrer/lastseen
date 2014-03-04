from django.conf.urls import patterns, include, url
# <<<<<<< HEAD
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# =======
from accounts.views import *
# >>>>>>> 36f0cd79ad43c4f33931978cb4ae3062c9198619
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^/', include('homepage.urls')),
	# url(r'^accounts/', include('accounts.urls')),
	url(r'^submission/', include('submission.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^signup/', signup),
	url(r'^accounts/profile/$', profile),
	url(r'^profile/(\d+)/$',singleprofile),
	url(r'^list/',accountList),
    url(r'^logout/',logout_view),
    url(r'^accounts/login/$',
        user_login, name = 'login'),
   url(r'^login/$', user_login),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# <<<<<<< HEAD
urlpatterns += staticfiles_urlpatterns()
# =======
# 	url(r'^admin/', include(admin.site.urls)),
# 	url(r'^signup/', signup),
# 	url(r'^account/profile$',profile, name= 'profilepage'),
# 	url(r'^profile/(\d+)/$',singleprofile),
# 	url(r'^list/',accountList),
# )
# >>>>>>> 36f0cd79ad43c4f33931978cb4ae3062c9198619
