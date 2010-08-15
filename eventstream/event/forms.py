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
    def clean_ended_at(self):
        """開始日時 < 終了日時バリデート
        """
        st = self.cleaned_data['started_at']
        ed = self.cleaned_data['ended_at']
        if st >= ed:
            raise forms.ValidationError(u'終了日時は開始日時以降に設定して下さい。')
        return ed

    class Meta:
        model = Event
        exclude = ('user','participants', 'lat', 'lng', 'created_at')

class ParticipateForm(forms.ModelForm):
    is_cancelled=forms.BooleanField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Participation
        fields = ('comment','is_cancelled')
