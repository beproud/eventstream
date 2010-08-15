from django.conf.urls.defaults import *

urlpatterns = patterns('account.views',
    url(r'^create$', 'create', name='create'),
)
