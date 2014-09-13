from django.conf.urls import patterns, url

__author__ = 'kishore-pc'

urlpatterns=patterns('',
    url('login', 'questioningsystem.views.fbLogin'),
    # url('(\w+)', ''),
    # url('add-question', ''),
)
