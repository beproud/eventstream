# -*- coding: utf-8 -*-
from django import forms

from account.models import Account

class AccountForm(forms.ModelForm):
    username = forms.CharField(label=u'ユーザー名')
    email = forms.EmailField(label=u'Email')

    def clean_username(self):
        """
        ユーザ名のユニークチェック
        """
        value = self.cleaned_data.get('username')
        value = value and value.strip()
        if self.instance._adding:
            valid = Account.objects.check_new_username(value)
        else:
            valid = Account.objects.check_new_username(value, self.instance.user.username)
        if not valid:
            raise forms.ValidationError(u'このユーザ名は既に存在しています')
        return value

    class Meta:
        model = Account
        fields = ['url', 'twitter_account', 'notify_email']
