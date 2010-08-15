# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template

from account.decorators import account_required

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
    """指定イベントの閲覧
    """
    return direct_to_template(request, 'event/detail.html', {
        'participate_form': ParticipateForm(),
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
    #TODO: ログインチェック
    #TOOD: 主催者チェック
    event.delete()
    return redirect('core:index')

@account_required
@event_view
def participate(request, event):
    form = ParticipateForm(request.POST)
    if form.is_valid():
        p = form.save(commit=False)
        p.user = request.account
        p.event = event
        p.save()
    return redirect(event) # イベント詳細ページ
