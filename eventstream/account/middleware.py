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
                try:
                    account = Account.objects.get_by_openid_url(openid_url=request.authinfo.url)
                except Account.DoesNotExist:
                    request.account = None
                else:
                    # 取得できた場合はセッションにも格納しておく
                    request.session[ACCOUNT_SESSION_KEY] = account
                    request.account = account
            else:
                request.account = None
