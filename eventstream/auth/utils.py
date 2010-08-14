# -*- coding: utf-8 -*-
from openid.consumer import consumer
from openid.store.filestore import FileOpenIDStore

from django.conf import settings
from django.core.urlresolvers import reverse

CONSUMER_SESSION_KEY = 'openid.consumer'
AUTHINFO_SESSION_KEY = 'auth.authinfo'

def has_consumer(request):
    return not not request.session.get(CONSUMER_SESSION_KEY)

def is_login(request):
    """
    requestがOpenID認証済みかを判定する関数
    authinfoに値があればTrueを返す
    """
    return not not request.session.get(AUTHINFO_SESSION_KEY)

def get_openid_realm():
    return 'http://%s/' % settings.DOMAIN

def get_openid_verify_url():
    return 'http://%s%s' % (settings.DOMAIN, reverse('auth_verify'))

def get_openid_request(openid_url):
    """
    リダイレクト先URLとconsumerオブジェクトを返す
    """
    # consumerオブジェクトを作ってリダイレクト先を取得
    c = consumer.Consumer({}, FileOpenIDStore(settings.OPENID_STORE_DIR))
    req = c.begin(openid_url)
    return req.redirectURL(get_openid_realm(), get_openid_verify_url()), c

def verify_openid_token(params, obj):
    """
    認証の検証を行って成功した場合のみOpenIDのURLを返す
    """
    res = obj.complete(params, get_openid_verify_url())
    if res.status == 'success':
        return res.identity_url

