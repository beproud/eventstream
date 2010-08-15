# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta

from django.db import models

from commons.decorators import cached_property
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
        return self.filter(user=account)

    def attending_by_account(self, account):
        """指定アカウントの参加イベント取得
        """
        return self.filter(participation__user=account, participation__is_cancelled=False)

    def cancelling_by_account(self, account):
        """指定アカウントのキャンセルイベント取得
        """
        return self.filter(participation__user=account, participation__is_cancelled=True)

    def now_events(self, now=None):
        """現在開催中のイベントを開催日時が古い順に取得
        """
        if now is None:
            now = datetime.now()
        return self.filter(started_at__lte=now, ended_at__gt=now).order_by('started_at')

    def today_events(self, today=None):
        """本日開催のイベントを開催日時が古い順に取得
        """
        if today is None:
            today = date.today()
        tommorow = today + timedelta(1)
        return self.filter(started_at__gte=today, started_at__lt=tommorow).order_by('started_at')

    def new_events(self):
        """最新登録されたイベントを作成日時が古い順に取得
        """
        #TODO:order_by('-created_at')
        return self.all().order_by('started_at')

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

    @cached_property
    def participants_count(self):
        """
        参加希望のカウント
        """
        return self.participation_set.attending().count()

    @cached_property
    def attendants(self):
        """
        正規 参加者
        """
        return self.participation_set.attending()[:self.member_limit] if self.member_limit > 0 else self.participation_set.none()

    @cached_property
    def waiting_list(self):
        """
        キャンセル待ち
        """
        return self.participation_set.attending()[self.member_limit:] if self.member_limit > 0 else self.participation_set.attending()

    @cached_property
    def cancelled(self):
        """
        キャンセルリスト
        """
        return self.participation_set.cancelled()
    
    @cached_property
    def cancelled_count(self):
        return len(self.waiting_list)

    @models.permalink
    def get_absolute_url(self):
        return ('event:detail', (self.id,), {}) 

    class Meta:
        db_table = 'event'
        verbose_name = verbose_name_plural = u'イベント'
        ordering = ['-started_at']

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
        ordering = ['is_cancelled', 'ctime']

    def __unicode__(self):
        return u'%s (%s)' % (self.event, self.user)
