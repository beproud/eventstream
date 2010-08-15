# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.utils.functional import wraps

from account.utils import has_account, LOGIN_REDIRECT_SESSION_KEY

def account_required(func):
    """
    アカウント情報がない場合にはアカウント情報作成へリダイレクト
    """
    def _inner(request, *args, **kwargs):
        if has_account(request):
            return func(request, *args, **kwargs)
        # リダイレクト先の保持
        request.session[LOGIN_REDIRECT_SESSION_KEY] = request.path
        return redirect('account:create')
    return wraps(func)(_inner)
