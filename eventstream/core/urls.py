#:coding=utf-8:

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
)
