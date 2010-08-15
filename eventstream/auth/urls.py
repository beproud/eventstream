from django.conf.urls.defaults import *

urlpatterns = patterns('auth.views',
    url(r'^login$', 'login', name='login'),
    url(r'^verify$', 'verify', name='verify'),
    url(r'^logout$', 'logout', name='logout'),
)
