from django.urls import path
from .views import *



urlpatterns = [
    path('<int:song_id>.html', CommentView, name='comment'),
]
