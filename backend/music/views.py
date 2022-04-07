from django.shortcuts import render

from music.models import Song


# from django.views.generic.list import ListView
# import logging
# from common.decorators import max_query_count


# logger = logging.getLogger(__name__)


# class SongsList(ListView):
#     model = Song
#     context_object_name = "songs"
#     template_name = "songs/songs_list.html"
#     queryset = Song.objects.select_related("album")


# @max_query_count(max_queries=1, logger=logger)
def songs_list(request):
    template_name = "songs/songs_list.html"
    context = {
        "songs": Song.objects.select_related("album"),
    }

    return render(request, template_name, context)
