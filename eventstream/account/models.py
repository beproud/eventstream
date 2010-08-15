# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class AccountManager(models.Manager):
    def create_user_account(self, username, email, password, openid_url, commit=True):
        """
        UserとAccountをまとめて作成
        commit=Falseとしてもuserは作成される
        """
        user = User.objects.create_user(username, email, password)
        account = self.model(user=user, openid_url=openid_url)
        if commit:
            account.save()
        return account

    def get_by_openid_url(self, openid_url, return_none=False):
        """
        openidのurlからアカウント情報を取得する
        """
        try:
            self.get_query_set().get(openid_url=openid_url)
        except self.model.DoesNotExist:
            if not return_none:
                raise

class Account(models.Model):
    """
    サイトのユーザアカウントモデル
    openid_urlは一意になるはず
    """
    user = models.ForeignKey(User, unique=True)
    openid_url = models.URLField(u'OpenID', verify_exists=False, unique=True) # OpenID認証用
    url = models.URLField(u'URL', verify_exists=False, null=True, blank=True)
    twitter_account = models.CharField(u'Twitter', max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(u'作成日時', default=datetime.now)
    notify_email = models.BooleanField(u'メールによる通知', default=True)

    objects = AccountManager()

    class Meta:
        db_table = 'account'
        verbose_name = verbose_name_plural = u'アカウント'
