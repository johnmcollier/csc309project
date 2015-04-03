from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import rest_framework

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kickstartupproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kickstartup/', include('kickstartup.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
