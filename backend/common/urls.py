# from django.conf import settings
from django.urls import include, path, re_path

from . import views


app_name = "common"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
