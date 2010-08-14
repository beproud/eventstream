from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

# static files for debug
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>.*\.(swf|pdf|jpg|JPG|gif|png|css|js|html|xml|ico))$',
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT })
    )
