# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template

from account.decorators import account_required

from commons.shortcuts import get_object_or_None

from event.decorators import event_view, owner_required
from event.forms import *
from event.models import * 

@account_required
def create(request):
    """
    イベント新規作成
    """

    frm = EventForm(request.POST or None)

    if request.method == 'POST' and frm.is_valid():
        event = frm.save(commit=False)
        event.user = request.account
        event.save()
        return redirect(event)

    return direct_to_template(request, 'event/create.html', {
        'frm': frm,
     })

@event_view
def detail(request, event):
    """
    指定イベントの閲覧
    """
    user_participation = get_object_or_None(Participation, user=request.account, event=event)
    # フォーム用 今の状態と逆
    is_cancelled = not user_participation.is_cancelled if user_participation else True  
    return direct_to_template(request, 'event/detail.html', {
        'participate_form': ParticipateForm(initial={'is_cancelled': is_cancelled}),
        'user_participation': user_participation,
        'event': event,
    })

@account_required
@event_view
@owner_required
def edit(request, event):
    """
    指定イベントの編集
    """

    frm = EventForm(request.POST or None, instance=event)
    if request.method == 'POST' and frm.is_valid():
        event = frm.save(commit=False)
        event.save()
        return redirect(event)

    return direct_to_template(request, 'event/edit.html', {
        'frm': frm,
    })

@account_required
@event_view
@owner_required
def delete(request, event):
    """
    指定イベントの削除
    """
    event.delete()
    return redirect('core:index')

@account_required
@event_view
def participate(request, event):
    p = get_object_or_None(Participation, user=request.account, event=event)
    if p:
        form = ParticipateForm(request.POST, instance=p)
    else:
        form = ParticipateForm(request.POST)
    if form.is_valid():
        p = form.save(commit=False)
        p.user = request.account
        p.event = event
        p.save()
    return redirect(event) # イベント詳細ページ
