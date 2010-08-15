# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class AccountManager(models.Manager):
    def create_user_account(self, username, email, openid_url, account=None, commit=True, **kwargs):
        """
        UserとAccountをまとめて作成
        commit=Falseとしてもuserは作成される
        """
        user = User.objects.create_user(username, email)
        # accountインスタンスを渡した場合
        if not account:
            account = self.model(user=user, openid_url=openid_url, **kwargs)
        else:
            account.user = user
            account.openid_url = openid_url
            for k, v in kwargs:
                setattr(account, k, v)
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

    def check_new_username(self, new_username, username=None):
        """
        新しいユーザ名として有効かどうかを判定する
        """
        if not new_username:
            return False
        # 同じ場合はok
        if username == new_username:
            return True
        # 既にあるかチェック
        return User.objects.filter(username=new_username).count() == 0

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
