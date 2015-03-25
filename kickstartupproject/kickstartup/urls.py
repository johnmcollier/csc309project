from django.conf.urls import patterns, url
from kickstartup import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'))
