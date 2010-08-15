from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^auth/', include('auth.urls', namespace="auth")),
    (r'^account/', include('account.urls', namespace="account")),
    (r'^admin/', include(admin.site.urls)),

    (r'^event/', include('event.urls', namespace="event")),
    (r'', include('core.urls', namespace="core")),
)

# static files for debug
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>.*\.(swf|pdf|jpg|JPG|gif|png|css|js|html|xml|ico))$',
         'django.views.static.serve', {'document_root': settings.SITE_MEDIA_ROOT })
    )
