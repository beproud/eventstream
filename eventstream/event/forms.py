# -*- coding:utf-8 -*-
from django import forms

from event.models import Event, Participation

__all__ = (
    'EventForm',
    'ParticipateForm',
)

class EventForm(forms.ModelForm):
    """イベント登録フォーム
    """
    class Meta:
        model = Event
        exclude = ('user','participants')

class ParticipateForm(forms.ModelForm):
    is_cancelled=forms.BooleanField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Participation
        fields = ('comment','is_cancelled')
