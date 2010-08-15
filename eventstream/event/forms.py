# -*- coding:utf-8 -*-
from django.forms import ModelForm

from event.models import Event, Participation

__all__ = (
    'EventForm',
    'ParticipateForm',
)

class EventForm(ModelForm):
    """イベント登録フォーム
    """
    class Meta:
        model = Event
        exclude = ('user','participants')

class ParticipateForm(ModelForm):
    class Meta:
        model = Participation
        fields = ('comment',)
