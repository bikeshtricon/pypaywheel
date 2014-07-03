from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'hr.views.index.dashboard', name='hrDashboard'),
    url(r'^(?P<reqId>\d+)/(?P<action>\w+)$', 'hr.views.index.leaveRequestsaction', name='acceptOrRegect'), 
)
