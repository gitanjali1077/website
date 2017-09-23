from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import *

class userProfile(models.Model):

    userName = models.OneToOneField(User)
    college = models.CharField(max_length=100)

    def __unicode__(self):  # __str__
        return unicode(self.userName)
