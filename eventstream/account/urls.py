from django.conf.urls.defaults import *

urlpatterns = patterns(
    'account.views',
    url(r'^check$', 'check', name='check'),
    url(r'^create$', 'create', name='create'),
    url(r'^edit$', 'edit', name='edit'),
    url(r'^(?P<account_id>\d+)$', 'detail', name='detail'),
)
