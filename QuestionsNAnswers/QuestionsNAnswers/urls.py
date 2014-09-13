from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QuestionsNAnswers.views.home', name='home'),
    # url(r'^QuestionsNAnswers/', include('QuestionsNAnswers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^qa/', include('questioningsystem.urls')),
    url(r'^api/', include('AnswerManagement.urls')),
    url(r'^mrnd/question', include('QuestionsManagement.urls'))
)
