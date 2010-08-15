# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.utils.functional import wraps

from account.utils import has_account

def account_required(func):
    """
    アカウント情報がない場合にはアカウント情報作成へリダイレクト
    """
    def _inner(request, *args, **kwargs):
        if has_account(request):
            return func(request, *args, **kwargs)
        # TODO: リダイレクト先の保持
        return redirect(reverse('account:account_create'))
    return wraps(func)(_inner)
