from datetime import datetime

from django.utils.timezone import utc

from music.models import *


def create_albums():
    Album.objects.bulk_create(
        [
            Album(
                album_title="Future Nostalgia",
                artist="Dua Lipa",
                release_date=datetime(2020, 3, 27, 3, 59, 0, 99999, tzinfo=utc),
                grammy_nominated=True,
            ),
            Album(
                album_title="Social Cues",
                artist="Cage The Elephant",
                release_date=datetime(2019, 4, 19, 3, 59, 0, 99999, tzinfo=utc),
                grammy_nominated=False,
            ),
            Album(
                album_title="Happier Than Ever",
                artist="Billie Eilish",
                release_date=datetime(2021, 7, 30, 3, 59, 0, 99999, tzinfo=utc),
                grammy_nominated=True,
            ),
            Album(
                album_title="Dreamland",
                artist="Glass Animals",
                release_date=datetime(2020, 8, 7, 3, 59, 0, 99999, tzinfo=utc),
                grammy_nominated=False,
            ),
            Album(
                album_title="The Colour and the Shape",
                artist="Foo Fighters",
                release_date=datetime(1997, 5, 20, 3, 59, 0, 99999, tzinfo=utc),
                grammy_nominated=True,
            ),
        ]
    )


def create_artists_composers():
    Artist.objects.bulk_create(
        [
            Artist(name="Billie Eilish", birthday=datetime(2001, 12, 18, 0, 0, 0, 0, tzinfo=utc)),
            Artist(
                name="Finneas O'Connell", birthday=datetime(1997, 7, 30, 0, 0, 0, 0, tzinfo=utc)
            ),
            Artist(name="Dave Bayley", birthday=datetime(1989, 6, 7, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Brittany Hazzard", birthday=datetime(1990, 6, 14, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Paul Epworth", birthday=datetime(1974, 7, 25, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Dua Lipa", birthday=datetime(1995, 8, 22, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Sarah Hudson", birthday=datetime(1984, 3, 24, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Julia Michaels", birthday=datetime(1993, 11, 13, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Dave Grohl", birthday=datetime(1969, 1, 14, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Matt Shultz", birthday=datetime(1983, 10, 23, 0, 0, 0, 0, tzinfo=utc)),
            Artist(name="Brad Shultz", birthday=datetime(1982, 5, 15, 0, 0, 0, 0, tzinfo=utc)),
            Artist(
                name="Cage The Elephant", birthday=datetime(1982, 5, 15, 0, 0, 0, 0, tzinfo=utc)
            ),
        ]
    )


def create_songs():
    artist_1 = Artist.objects.get(name="Billie Eilish")
    artist_2 = Artist.objects.get(name="Finneas O'Connell")
    artist_3 = Artist.objects.get(name="Dave Bayley")
    artist_4 = Artist.objects.get(name="Brittany Hazzard")
    artist_5 = Artist.objects.get(name="Paul Epworth")
    artist_6 = Artist.objects.get(name="Matt Shultz")
    artist_7 = Artist.objects.get(name="Brad Shultz")
    artist_8 = Artist.objects.get(name="Cage The Elephant")
    artist_9 = Artist.objects.get(name="Dave Grohl")
    artist_10 = Artist.objects.get(name="Dua Lipa")
    artist_11 = Artist.objects.get(name="Sarah Hudson")
    artist_12 = Artist.objects.get(name="Julia Michaels")

    future_nostalgia = Album.objects.get(album_title="Future Nostalgia", artist="Dua Lipa")
    social_cues = Album.objects.get(album_title="Social Cues", artist="Cage The Elephant")
    hte = Album.objects.get(album_title="Happier Than Ever", artist="Billie Eilish")
    dreamland = Album.objects.get(album_title="Dreamland", artist="Glass Animals")
    tcts = Album.objects.get(album_title="The Colour and the Shape", artist="Foo Fighters")

    song_1 = Song.objects.create(
        song_title="Everything I Wanted",
        release_date=datetime(2019, 11, 13, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.pop_music,
        grammy_nominated=True,
    )
    song_1.composers.set([artist_1, artist_2])
    song_2 = Song.objects.create(
        song_title="No Time To Die",
        release_date=datetime(2020, 2, 13, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.pop_music,
        grammy_nominated=True,
    )
    song_2.composers.set([artist_1, artist_2])
    song_3 = Song.objects.create(
        song_title="I Dont Wanna Talk (I Just Wanna Dance)",
        release_date=datetime(2020, 12, 13, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.pop_music,
        grammy_nominated=False,
    )
    song_3.composers.set([artist_3])

    song_4 = Song.objects.create(
        song_title="Electricity",
        release_date=datetime(2018, 9, 6, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.electronic_music,
        grammy_nominated=True,
    )
    song_4.composers.set([artist_10])

    # Future Nostalgia songs
    song_5 = future_nostalgia.songs.create(
        song_title="Pretty Please",
        release_date=datetime(2020, 3, 27, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.pop_music,
        grammy_nominated=False,
    )
    song_5.composers.set([artist_10, artist_12])
    song_6 = future_nostalgia.songs.create(
        song_title="Levitating",
        release_date=datetime(2020, 3, 27, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.pop_music,
        grammy_nominated=False,
    )
    song_6.composers.set([artist_10, artist_11])

    # Social Cues songs
    song_7 = social_cues.songs.create(
        song_title="Social Cues",
        release_date=datetime(2019, 4, 19, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.rock,
        grammy_nominated=False,
    )
    song_7.composers.set([artist_6, artist_7])
    song_8 = social_cues.songs.create(
        song_title="Skin and Bones",
        release_date=datetime(2019, 4, 19, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.rock,
        grammy_nominated=False,
    )
    song_8.composers.set([artist_8])

    # Happier Than Ever songs
    song_9 = hte.songs.create(
        song_title="NDA",
        release_date=datetime(2021, 7, 9, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.electronic_music,
        grammy_nominated=False,
    )
    song_9.composers.set([artist_1, artist_2])
    song_10 = hte.songs.create(
        song_title="Your Power",
        release_date=datetime(2021, 4, 29, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.pop_music,
        grammy_nominated=True,
    )
    song_10.composers.set([artist_1, artist_2])
    song_11 = hte.songs.create(
        song_title="Oxytocin",
        release_date=datetime(2021, 7, 30, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.electronic_music,
        grammy_nominated=False,
    )
    song_11.composers.set([artist_1, artist_2])

    # Dreamland songs
    song_12 = dreamland.songs.create(
        song_title="Tangerine",
        release_date=datetime(2020, 8, 7, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.rock,
        grammy_nominated=False,
    )
    song_12.composers.set([artist_3, artist_4, artist_5])
    song_13 = dreamland.songs.create(
        song_title="Heat Waves",
        release_date=datetime(2020, 6, 29, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.pop_music,
        grammy_nominated=False,
    )
    song_13.composers.set([artist_3])
    song_14 = dreamland.songs.create(
        song_title="Helium",
        release_date=datetime(2020, 8, 7, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.rock,
        grammy_nominated=False,
    )
    song_14.composers.set([artist_3])

    # The Colour and the Shape songs
    song_15 = tcts.songs.create(
        song_title="Everlong",
        release_date=datetime(1997, 8, 18, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.rock,
        grammy_nominated=False,
    )
    song_15.composers.set([artist_9])
    song_16 = tcts.songs.create(
        song_title="Monkey Wrench",
        release_date=datetime(1997, 4, 28, 3, 59, 0, 99999, tzinfo=utc),
        genre=MUSIC_GENRES_CHOICES.rock,
        grammy_nominated=False,
    )
    song_16.composers.set([artist_9])


def clean_database():
    Song.objects.all().delete()
    Artist.objects.all().delete()
    Album.objects.all().delete()
