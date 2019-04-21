from django.urls import path
from .views import *


urlpatterns = [
    path('', RankingView, name='ranking'),
    # 通用视图
    path('.list', RankingList.as_view(), name='rankingList'),
]
