#from __future__ import unicode_literals

from django.db import models

# required for forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Album(models.Model):
    artist =models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

#here u pass the url and then give the page to display aloong with it needs the pk of
#the object
    #which is an hideen element right here so we are using(keywordargs) kwargs here

    def get_absolute_url(self):
        return reverse('notes:detail' ,kwargs={'pk': self.pk})


    def __str__(self):
        return self.album_title + ' - ' + self.artist 

class Song(models.Model):
    album= models.ForeignKey(Album , on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title =models.CharField(max_length=300)
    
    def __str__(self):
        return self.song_title

class users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    college= models.CharField(max_length=200)

    def __str__(self):
        return self.username


