# -*- coding: utf-8 -*-
import urllib

from django.conf import settings
from django.utils.hashcompat import md5_constructor
from django.utils.html import escape

ACCOUNT_SESSION_KEY = 'account'
LOGIN_REDIRECT_SESSION_KEY = 'account.redirect_path'
GRAVATAR_URL_PREFIX = getattr(settings, 'GRAVATAR_URL_PREFIX', 'http://www.gravatar.com/')

def has_account(request):
    """
    アカウント情報がセッションにあるかどうか
    """
    return not not request.session.get(ACCOUNT_SESSION_KEY)

def gravatar_for_email(email, size=None):
    """
    メールアドレスからgravatarのURLを返す
    """
    url = '%savatar/%s/' % (GRAVATAR_URL_PREFIX, md5_constructor(email.lower()).hexdigest())
    if not size:
        size = 80  
    url += '?' + urllib.urlencode({'s': str(size)})
    return escape(url)
