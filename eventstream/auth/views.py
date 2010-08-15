# -*- coding: utf-8 -*-
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template
from django.conf import settings

from auth.decorators import consumer_reqiured, login_required
from auth.utils import get_openid_request, verify_openid_token, CONSUMER_SESSION_KEY, AUTHINFO_SESSION_KEY
from auth.forms import LoginForm
from auth.models import AuthInfo

def login(request):
    """
    ログイン
    """
    form = LoginForm(request.POST or None)
    if form.is_valid():
        url, obj = get_openid_request(form.cleaned_data['openid_url'])
        # セッションにトークンを保持
        request.session[CONSUMER_SESSION_KEY] = obj
        # OpenID認証ページへリダイレクト
        return redirect(url)
    return direct_to_template(request, 'auth/login.html', {'form': form})

@consumer_reqiured
def verify(request):
    """
    OpenIDの検証
    """
    obj = request.session[CONSUMER_SESSION_KEY]
    url = verify_openid_token(request.GET, obj)
    if url:
        # AuthInfoを作成してセッションに保持
        request.session[AUTHINFO_SESSION_KEY] = AuthInfo(url)
        del request.session[CONSUMER_SESSION_KEY]
        return redirect(settings.LOGIN_REDIRECT_URL)
    return HttpResponseBadRequest(u'bad openid')

#@login_required
def logout(request):
    """
    ログアウトページ
    """
    request.session.flush()
    if hasattr(request, "account"):
        request.account = None
    if hasattr(request, "authinfo"):
        request.authinfo = None
    return redirect('core:index')
