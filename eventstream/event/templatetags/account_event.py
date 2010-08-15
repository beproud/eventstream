# -*- coding:utf-8 -*-
from django import template

from commons.utils.template import data_template_tag

from event.models import Event


register = template.Library()

@register.tag
@data_template_tag
def get_managing_events(account):
    """指定アカウントが管理しているイベントのクエリセットを取得
    """
    return Event.objects.managing_by_account(account)

@register.tag
@data_template_tag
def get_attending_events(account):
    """指定アカウントが参加しているイベントのクエリセットを取得
    """
    return Event.objects.attending_by_account(account)

@register.tag
@data_template_tag
def get_cancelling_events(account):
    """指定アカウントがキャンセルしているイベントのクエリセットを取得
    """
    return Event.objects.cancelling_by_account(account)
