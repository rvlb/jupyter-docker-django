from django.shortcuts import render
from django.views.generic.list import ListView

from music.models import Song


class SongsList(ListView):
    model = Song
    context_object_name = "songs"
    template_name = "songs/songs_list.html"
