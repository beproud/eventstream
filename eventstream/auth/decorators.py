# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.utils.functional import wraps

from auth.utils import has_consumer, is_login

def consumer_reqiured(func):
    """
    consumerオブジェクトがセッションにない場合にはloginへリダイレクト
    """
    def _inner(request, *args, **kwargs):
        if has_consumer(request):
            return func(request, *args, **kwargs)
        return redirect(reverse('auth_login'))
    return wraps(func)(_inner)

def login_required(func):
    """
    OpenIDで認証していない場合にはloginへリダイレクト
    """
    def _inner(request, *args, **kwargs):
        if is_login(request):
            return func(request, *args, **kwargs)
        return redirect(reverse('auth_login'))
    return wraps(func)(_inner)
