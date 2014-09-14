from django.conf.urls import patterns, url

__author__ = 'kishore-pc'

urlpatterns=patterns('questioningsystem.views',
    url('login', 'fbLogin'),
    url('api','apifblogin'),
    # url('(\w+)', ''),
    # url('add-question', ''),
)
