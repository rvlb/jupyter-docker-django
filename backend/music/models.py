from django.db import models


# Create your models here.


class Album(models.Model):
    album_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.album_title} by {self.artist}"


class Song(models.Model):
    song_title = models.CharField(max_length=200)
    album = models.ForeignKey(
        "music.Album", related_name="songs", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.song_title
