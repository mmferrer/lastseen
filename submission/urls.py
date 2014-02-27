from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
	url(r'^$', views.ListSubmissionView.as_view(), name='submission-list',),
	url(r'^new$', views.CreateSubmissionView.as_view(), name='submission-new',),
	url(r'^edit/(?P<pk>\d+)/$', views.UpdateSubmissionView.as_view(), name='submission-edit',),
	url(r'^delete/(?P<pk>\d+)/$', views.DeleteSubmissionView.as_view(), name='submission-delete',),
	url(r'^(?P<pk>\d+)/$', views.SubmissionView.as_view(), name='submission-view',),
)