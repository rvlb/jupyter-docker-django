from django.db import models

from music.choices import MUSIC_GENRES_CHOICES


class RecordCompany(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    album_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    record_company = models.ForeignKey(
        "music.RecordCompany", related_name="albums", on_delete=models.CASCADE, null=True
    )
    release_date = models.DateTimeField(null=True)
    grammy_nominated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.album_title} by {self.artist}"


class Artist(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    song_title = models.CharField(max_length=200)
    album = models.ForeignKey(
        "music.Album", related_name="songs", on_delete=models.CASCADE, null=True
    )
    composers = models.ManyToManyField("music.Artist", related_name="songs_written", blank=True)
    genre = models.CharField(choices=MUSIC_GENRES_CHOICES, max_length=200, blank=True)
    release_date = models.DateTimeField(null=True)
    grammy_nominated = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
