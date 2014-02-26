from django.conf.urls import patterns, include, url
from accounts.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lastseen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^signup/', signup),
    url(r'^account/profile$',profile, name= 'profilepage'),
    (r'^profile/(\d+)/$',singleprofile),
    (r'^list/',accountList),
)
