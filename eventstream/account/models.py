# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class AccountManager(models.Manager):
    pass

class Account(models.Model):
    """
    サイトのユーザアカウントモデル
    openid_urlは一意になるはず
    """
    user = models.ForeignKey(User, unique=True)
    openid_url = models.URLField(u'OpenID', verify_exists=False, unique=True) # OpenID認証用
    name = models.CharField(u'アカウント名', max_length=20)
    url = models.URLField(u'URL', verify_exists=False, null=True, blank=True)
    twitter_account = models.CharField(u'Twitter', max_length=20)
    created_at = models.DateTimeField(u'作成日時', default=datetime.now)
    notify_email = models.BooleanField(u'メールによる通知', default=True)

    objects = AccountManager()

    class Meta:
        db_table = 'account'
        verbose_name = verbose_name_plural = u'アカウント'
