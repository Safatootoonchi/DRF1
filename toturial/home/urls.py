from django.urls import path
from .views import *


urlpatterns = [
    path("s/", snippet_list),
    path("s/<int:pk>", snippet_detail),
]
