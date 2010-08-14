# -*- coding:utf-8 -*-
from django.forms import ModelForm

from event.models import Event


class EventForm(ModelForm):
    """イベント登録フォーム
    """
    class Meta:
        model = Event
        exclude = ('user',)
