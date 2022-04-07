from django.urls import re_path

from music.views import songs_list


app_name = "music"

urlpatterns = [
    # re_path(r"^songs/list/", SongsList.as_view()),
    re_path(r"^songs/list/", songs_list, name="songs"),
]
