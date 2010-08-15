#:coding=utf-8:

from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from event.models import *

from models import *
from forms import *

def index(request):
    return direct_to_template(request, 'core/index.html', extra_context = {
            'now_events': Event.objects.now_events()[:10],
            'today_events': Event.objects.today_events()[:10],
            'new_events': Event.objects.new_events()[:10],
            })
