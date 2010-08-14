# -*- coding: utf-8 -*-
from account.utils import has_account, ACCOUNT_SESSION_KEY
from account.models import Account

class AccountMiddleware(object):
    def process_request(self, request):
        """
        セッションのアカウント情報をrequestに付与する
        アカウント情報がない場合はaccountにNoneを入れる
        request.authinfoがある場合はDBにアカウントを問い合わせる

          if request.account:
              # アカウント有
          else:
              # アカウント無

        のように利用する
        """
        if has_account(request):
            request.account = request.session.get(ACCOUNT_SESSION_KEY)
        else:
            if getattr(request, 'authinfo', None):
                request.account = Account.objects.get_by_openid_url(openid_url=request.authinfo.url, return_none=True)
            else:
                request.account = None
