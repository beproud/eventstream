# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from account.models import Account

__all__ = (
    'Event',
    'Participation',
)

class EventManager(models.Manager):
    """
    イベントマネージャ
    """
    def managing_by_account(self, account):
        """
        指定アカウント主催のイベント取得
        """
        return self.filter(user=account).order_by('-started_at')

    def attending_by_account(self, account):
        """指定アカウントの参加情報取得
        """
        return self.filter(participation__user=account, participation__is_cancelled=False).order_by('-started_at')

class Event(models.Model):
    """
    イベントモデル
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

    participants = models.ManyToManyField(
        Account,
        verbose_name=u"参加者",
        through="Participation",
        related_name="user_events",
        blank=True,
        null=True,
    )
    # TODO: 正規 参加者
    # TODO: キャンセル待ち
    # TODO: キャンセルリスト

    @models.permalink
    def get_absolute_url(self):
        return ('event:detail', (self.id,), {}) 

    class Meta:
        db_table = 'event'
        verbose_name = verbose_name_plural = u'イベント'

    def __unicode__(self):
        return u'%s: %s' % (self.id, self.name)

class ParticipationManager(models.Manager):
    def attending(self):
        """参加情報取得
        """
        return self.filter(is_cancelled=False)

    def cancelled(self):
        """キャンセル情報取得
        """
        return self.filter(is_cancelled=True)

class Participation(models.Model):
    """イベント参加管理モデル
    """
    user = models.ForeignKey(Account, verbose_name=u"参加者")
    event = models.ForeignKey(Event, verbose_name=u"イベント")
    comment = models.TextField(u'コメント', max_length=1000, blank=True)
    is_cancelled = models.BooleanField(u"キャンセル？", default=False)
    
    ctime = models.DateTimeField(u'作成日時', default=datetime.now, db_index=True)
    utime = models.DateTimeField(u'更新日時', auto_now=True, db_index=True)

    objects = ParticipationManager()

    class Meta:
        db_table = 'event_participation'
        verbose_name = verbose_name_plural = u'イベント参加'
        unique_together = (("user", "event"),)
        ordering = ['is_cancelled', '-ctime']

    def __unicode__(self):
        return u'%s (%s)' % (self.event, self.user)
