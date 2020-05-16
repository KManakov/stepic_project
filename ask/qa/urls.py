from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', name='index'),
    url(r'^popular/.*$', name='popular'),    
    url(r'^ask/.*$', name='ask'),
    url(r'^answer/.*$', name='answer'),
    url(r'^signup/.*$', name='signup'),
    url(r'^login/.*$', name='login'),
    url(r'^logout/.*$', name='logout'),    
    url(r'^new/.*$'),
    url(r'^question/(?P<question_id>[0-9]+)/$', name='question'),    
]