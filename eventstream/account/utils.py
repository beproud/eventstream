# -*- coding: utf-8 -*-
ACCOUNT_SESSION_KEY = 'account'

def has_account(request):
    """
    アカウント情報がセッションにあるかどうか
    """
    return not not request.session.get(ACCOUNT_SESSION_KEY)
