# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import wraps

from event.models import Event


def owner_required(func):
    """指定イベントの主催者によるアクセスかチェック
    """
    def _inner(request, event_id, *args, **kwargs):
        event = get_object_or_404(Event, pk=event_id)
        if request.account == event.user:
            return func(request, event, *args, **kwargs)
        return redirect(reverse('core:index'))
    return wraps(func)(_inner)
