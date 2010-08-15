# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect, get_object_or_404

from auth.decorators import login_required
from account.utils import LOGIN_REDIRECT_SESSION_KEY
from account.forms import AccountForm
from account.models import Account

def check(request):
    """
    ログイン直後の遷移先
    Accountをチェックしてリダイレクトする
    """
    if request.account:
        # 保持しておいたリダイレクト先があれば使う
        redirect_name = request.session.get(LOGIN_REDIRECT_SESSION_KEY, 'core:index')
        return redirect(redirect_name)
    return redirect('account:create')

@login_required
def create(request):
    """
    アカウント情報作成ページ
    """
    form = AccountForm(request.POST or None)
    if form.is_valid():
        Account.objects.create_user_account(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            openid_url=request.authinfo.url,
            account=form.instance,
        )
        return redirect('account:check')
    return direct_to_template(request, 'account/create.html', {'form': form})

def detail(request, account_id):
    """指定アカウント詳細ページ
    """
    account = get_object_or_404(Account, pk=account_id)
    return direct_to_template(request, 'account/detail.html', {'target_account': account})
