# -*- coding:utf-8 -*-
from django.contrib import admin

from event.models import Event, Participation

admin.site.register(Event)
admin.site.register(Participation)
