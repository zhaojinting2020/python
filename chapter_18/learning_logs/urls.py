"""Defines url patterns for learning_logs."""

from django.conf.urls import include, url

from django.contrib import admin

from . import views

urlpatterns = [

    # Home page.
    url(r'^$', views.index, name='index'),
    
    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),
    
    # Detail page for a single topic.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]
