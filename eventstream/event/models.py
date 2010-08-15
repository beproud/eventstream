# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from account.models import Account


class EventManager(models.Manager):
    """イベントマネージャ
    """
    def by_account(self, account):
        """指定アカウント主催のイベント取得
        """
        return self.filter(user=account)

class Event(models.Model):
    """イベントモデル
    """
    objects = EventManager()

    user = models.ForeignKey(Account)
    name = models.CharField(u'タイトル', max_length=255)
    description = models.TextField(u'説明', max_length=1000, blank=True)
    body = models.TextField(u'内容', max_length=1000)
    member_limit = models.IntegerField(u'定員', blank=True, null=True)
    place = models.CharField(u'会場', max_length=255, blank=True, null=True)
    address = models.CharField(u'住所', max_length=255, blank=True, null=True)
    hashtag = models.CharField(u'Twitterハッシュタグ', max_length=100, blank=True, null=True)
    started_at = models.DateTimeField(u'開始日時', default=datetime.now)
    ended_at = models.DateTimeField(u'終了日時', default=datetime.now)

    @models.permalink
    def get_absolute_url(self):
        return ('event:detail', (self.id,), {}) 

    class Meta:
        db_table = 'event'
        verbose_name = verbose_name_plural = u'イベント'

    def __unicode__(self):
        return u'%s: %s' % (self.id, self.name)
