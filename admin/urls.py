from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypaywheel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'admin.views.home', name='home'),
)
