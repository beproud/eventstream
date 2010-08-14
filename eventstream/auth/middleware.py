# -*- coding: utf-8 -*-
from auth.utils import is_login, AUTHINFO_SESSION_KEY

class AuthInfoMiddleware(object):
    def process_request(self, request):
        """
        認証情報をrequestに付与する
        未認証の場合はauthinfoにNoneを入れる

          if request.authinfo:
              # 認証済み
          else:
              # 未認証

        のように利用する
        """
        if is_login(request):
            request.authinfo = request.session.get(AUTHINFO_SESSION_KEY)
        else:
            request.authinfo = None
