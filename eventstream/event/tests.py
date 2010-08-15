# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.test import TestCase

from account.models import Account
from event.models import Event

class EventModelTest(TestCase):
    def setUp(self):
        self.now = datetime.now()
        
        # Account
        self.a1 = Account.objects.create_user_account(
            username='user1',
            email='user1@example.com',
            openid_url='http://example.com/user1/',
            )

        self.a2 = Account.objects.create_user_account(
            username='user2',
            email='user2@example.com',
            openid_url='http://example.com/user2/',
            )

        # Event
        self.ev1 = Event.objects.create(
            user=self.a1,
            name=u'event1',
            body=u'My first event :)',
            started_at=self.now,
            ended_at=self.now + timedelta(2)
            )

    def tearDown(self):
        pass

    def test_eventmanager_managing_by_account(self):
        """EventManager.managing_by_account テスト
        """
        events = Event.objects.managing_by_account(self.a1)
        self.assertEqual(events.count(), 1)

        events = Event.objects.managing_by_account(self.a2)
        self.assertEqual(events.count(), 0)
