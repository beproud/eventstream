# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from auth.decorators import login_required
from account.forms import AccountForm
from account.models import Account

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
        # TODO: リダイレクト保持
        return redirect(reverse('index'))
    return direct_to_template(request, 'account/create.html', {'form': form})
