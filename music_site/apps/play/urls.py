from django.urls import path
from .views import *


urlpatterns = [
    path('<int:song_id>.html', PlayView, name='play'),
    path('download/<int:song_id>.html', DownloadView, name='download'),
]
