# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template

from account.decorators import account_required

from event.forms import EventForm
from event.models import Event
from event.decorators import owner_required


@account_required
def create(request):
    """イベント新規作成
    """
    frm = EventForm(request.POST or None)

    if request.method == 'POST' and frm.is_valid():
        event = frm.save(commit=False)
        event.user = request.account
        event.save()
        return redirect('event:detail', event_id=event.id)

    return direct_to_template(request, 'event/create.html', {
            'frm': frm,
            })

def detail(request, event_id):
    """指定イベントの閲覧
    """
    event = get_object_or_404(Event, pk=event_id)
    return direct_to_template(request, 'event/detail.html', {
            'event': event,
            })

@account_required
@owner_required
def edit(request, event):
    """指定イベントの編集
    """
    frm = EventForm(request.POST or None, instance=event)

    if request.method == 'POST' and frm.is_valid():
        event = frm.save(commit=False)
        event.save()
        return redirect('event:detail', event_id=event.id)

    return direct_to_template(request, 'event/edit.html', {
            'frm': frm,
            })

@account_required
@owner_required
def delete(request, event):
    """指定イベントの削除
    """
    event.delete()
    return redirect('core:index')
