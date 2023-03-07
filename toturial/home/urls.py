from django.urls import path
from .views import *


urlpatterns = [
    path("s/", SnippetList.as_view()),
    path("s/<int:pk>", SnippetDetail.as_view()),
]
