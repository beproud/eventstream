# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'event.views',
    url(r'^new$', 'create', name='create'),
    url(r'^(?P<event_id>\d+)$', 'detail', name='detail'),
    url(r'^(?P<event_id>\d+)/edit$', 'edit', name='edit'),
    url(r'^(?P<event_id>\d+)/delete$', 'delete', name='delete'),
    url(r'^(?P<event_id>\d+)/participate$', 'participate', name='participate'),

    url(r'^list/(?P<list_type>\w+)/$', 'event_list', name='list'),
)
