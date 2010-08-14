# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'event.views',
    url(r'^$', 'index', name='index'),
    url(r'^new$', 'create', name='event_create'),
    url(r'^(?P<event_id>\d+)$', 'detail', name='event_detail'),
    url(r'^(?P<event_id>\d+)/edit$', 'edit', name='event_edit'),
    url(r'^(?P<event_id>\d+)/delete$', 'delete', name='event_delete'),
    )
