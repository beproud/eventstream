# -*- coding: utf-8 -*-
from datetime import datetime

class AuthInfo(object):
    """
    認証情報
    """
    def __init__(self, url, created_at=None):
        self.url = url
        if not created_at:
            created_at = datetime.now()
        self.created_at = created_at
