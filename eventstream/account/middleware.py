# -*- coding: utf-8 -*-
from account.utils import has_account, ACCOUNT_SESSION_KEY

class AccountMiddleware(object):
    def process_request(self, request):
        """
        セッションのアカウント情報をrequestに付与する
        アカウント情報がない場合はaccountにNoneを入れる

          if request.account:
              # アカウント有
          else:
              # アカウント無

        のように利用する
        """
        if has_account(request):
            request.account = request.session.get(ACCOUNT_SESSION_KEY)
        else:
            request.account = None
