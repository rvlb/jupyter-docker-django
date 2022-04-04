# from django.conf import settings
from django.urls import include, path, re_path

from . import views


app_name = "common"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    re_path(r"^music/", include("music.urls")),
]


# if "silk" in settings.INSTALLED_APPS:
#         urlpatterns += [re_path(r"^silk/", include("silk.urls", namespace="silk"))]
