# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    openid_url = forms.CharField(label=u'OpenID', max_length=1024)
