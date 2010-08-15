# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

from event.models import Event

urlpatterns = patterns(
    'event.views',
    url(r'^new$', 'create', name='create'),
    url(r'^(?P<event_id>\d+)$', 'detail', name='detail'),
    url(r'^(?P<event_id>\d+)/edit$', 'edit', name='edit'),
    url(r'^(?P<event_id>\d+)/delete$', 'delete', name='delete'),
    url(r'^(?P<event_id>\d+)/participate$', 'participate', name='participate'),
    )

# 一覧系
now_list_dict = {
    'queryset': Event.objects.now_events(),
    'template_name': 'event/now_list.html',
    'paginate_by': 100,
    }
today_list_dict = {
    'queryset': Event.objects.today_events(),
    'template_name': 'event/today_list.html',
    'paginate_by': 100,
    }
new_list_dict = {
    'queryset': Event.objects.new_events(),
    'template_name': 'event/new_list.html',
    'paginate_by': 100,
    }
urlpatterns += patterns(
    '',
    url(r'^list/now/$', 'django.views.generic.list_detail.object_list', now_list_dict, name='now_list'),
    url(r'^list/today/$', 'django.views.generic.list_detail.object_list', today_list_dict, name='today_list'),
    url(r'^list/new/$', 'django.views.generic.list_detail.object_list', new_list_dict, name='new_list'),
    )
