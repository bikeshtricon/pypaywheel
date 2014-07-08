from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypaywheel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hr/', include('hr.urls')),
    url(r'^login/', 'pypaywheel.views.login.log_in'),
    url(r'^logout/', 'pypaywheel.views.login.logout_view'),
    
    url(r'^dashboard/', 'pypaywheel.views.login.dashboard'),
)
