# -*- coding: utf-8 -*-
from django.test import TestCase

from account.models import Account

class AccountTestCase(TestCase):
    def test_create_account(self):
        """
        アカウント作成テスト
        """
        self.account = Account.objects.create_user_account(
            username='user1',
            email='user1@example.com',
            password='password1',
            openid_url='http://example.com/user1/',
            nickname='nick1'
        )
