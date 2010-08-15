# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

from event.forms import EventForm
from event.models import Event

#@login_required
def create(request):
    """イベント新規作成
    """
    #TODO: ログインチェック

    frm = EventForm(request.POST or None)

    if request.method == 'POST' and frm.is_valid():
        event = frm.save(commit=False)
        event.user = request.account #TODO: ログインユーザーのアカウントにする
        event.save()
        return HttpResponseRedirect(reverse('event:detail', kwargs={'event_id': event.id}))

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

#@owner_required
def edit(request, event_id):
    """指定イベントの編集
    """
    #TODO: ログインチェック
    #TOOD: 主催者チェック

    event = get_object_or_404(Event, pk=event_id)
    frm = EventForm(request.POST or None, instance=event)

    if request.method == 'POST' and frm.is_valid():
        event = frm.save(commit=False)
        event.save()
        return HttpResponseRedirect(reverse('event_detail', kwargs={'event_id': event.id}))

    return direct_to_template(request, 'event/edit.html', {
            'frm': frm,
            })

#@owner_required
def delete(request, event_id):
    """指定イベントの削除
    """
    #TODO: ログインチェック
    #TOOD: 主催者チェック

    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return HttpResponseRedirect(reverse('index'))
