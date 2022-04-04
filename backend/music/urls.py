from django.urls import re_path

from music.views import SongsList


app_name = "music"

urlpatterns = [
    re_path(r"^songs/list/", SongsList.as_view()),
]
