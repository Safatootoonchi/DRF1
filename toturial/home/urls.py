
from django.urls import path
from .views import *


urlpatterns = [
    path("album/", AlbumList.as_view()),
    path("album/<int:pk>", AlbumDetail.as_view()),
]