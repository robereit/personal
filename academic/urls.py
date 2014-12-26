from django.conf.urls import patterns, url

from academic import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^papers/$', views.papers, name='papers'),
    url(r'^teaching/$', views.teaching, name='teaching')
)
