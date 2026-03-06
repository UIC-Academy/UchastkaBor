from django.urls import path

from apps.estate.views import home


urlpatterns = [
    path("", home),
]
