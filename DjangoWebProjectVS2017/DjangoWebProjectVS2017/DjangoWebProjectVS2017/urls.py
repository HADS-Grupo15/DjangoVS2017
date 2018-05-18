"""
Definition of urls for DjangoWebProjectVS2017.
"""

from datetime import datetime
from django.conf.urls import include,url
from django.contrib import admin
import django.contrib.auth.views

import app.forms
import app.views
import app.models

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^user/', app.views.user_new, name='user'),
    url(r'^users/', app.views.users_detail, name='users_detail'),
    url(r'^chart/(?P<question_id>\d+)/$', app.views.chart, name='chart'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/add/', app.views.question_new, name='add'),
    url(r'^polls/choice_add/(?P<question_id>\d+)/$', app.views.choice_add, name='choice_add'),
    url(r'^(?P<question_id>\d+)/results/$', app.views.results, name='results'),
    url(r'^polls/(?P<question_id>\d+)/$', app.views.detail, name='detail'),
    url(r'^polls/(?P<question_id>\d+)/vote/$', app.views.vote, name='vote'),
    url(r'^polls/', app.views.index, name='index'),
    url(r'^quiz/add/', app.views.Quiz_question_new, name='qadd'),
    url(r'^quiz/choice_add/(?P<question_id>\d+)/$', app.views.Quiz_choice_add, name='qchoice_add'),
    url(r'^(?P<question_id>\d+)/qresults/$', app.views.Quiz_results, name='qresults'),####
    url(r'^(?P<question_id>\d+)/results/correct$', app.views.Quiz_results2, name='correct'),
    url(r'^(?P<question_id>\d+)/results/incorrect$', app.views.Quiz_results3, name='incorrect'),
    url(r'^quiz/(?P<question_id>\d+)/$', app.views.Quiz_detail, name='qdetail'),
    url(r'^quiz/(?P<question_id>\d+)/vote/$', app.views.Quiz_vote, name='qvote'),
    url(r'^quiz/$', app.views.Quiz_index, name='qindex'),
    #url(r'^quiz/(?P<topic_str>\w+)/$', app.views.Quiz_index_bytopic, name='qindexbytopic'),
    url(r'^quiz/chart/(?P<question_id>\d+)/$', app.views.Quiz_chart, name='qchart'),
   
]