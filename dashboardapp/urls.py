from django.conf.urls import patterns,  url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'dashboardapp.views.login.log_in', name='home'),
    
)
