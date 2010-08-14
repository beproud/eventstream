from django.db import models

class EventManager(models.Manager):
    """Event model manager
    """
    def by_account(self, account):
        """Return event query-set related with the account.
        """
        return self.filter(user=account)

class Event(models.Model):
    """Event model
    """
    object = EventManager()

    user = models.ForeignKey('account.Account')
    name = models.CharField('Title', max_length=255)
    description = models.TextField('Event Description', max_length=1000, blank=True)
    body = models.TextField('Body Text', max_length=1000)
    member_limit = models.IntegerField('Member Limit', blank=True, null=True)
    place = models.CharField('Place', max_length=255, blank=True, null=True)
    address = models.CharField('Address', max_length=255, blank=True, null=True)
    hashtag = models.CharField('Twitter Hashtag', max_length=100, blank=True, null=True)
    started_at = models.DateTimeField('Start Time')
    ended_at = models.DateTimeField('End TIme')

    class Meta:
        db_table = 'event'

    def __unicode__(self):
        return u'%s: %s' % (self.id, self.name)

