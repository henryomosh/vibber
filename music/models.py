from django.db import models
from django.contrib.auth.models import Permission, User


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_art = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.artist + '-' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


class Paper(models.Model):
    logo = models.FileField(default='')
