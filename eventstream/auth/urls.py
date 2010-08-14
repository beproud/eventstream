from django.conf.urls.defaults import *

urlpatterns = patterns('auth.views',
    url(r'^login$', 'login', name='auth_login'),
    url(r'^verify$', 'verify', name='auth_verify'),
    url(r'^logout$', 'logout', name='auth_logout'),
)
