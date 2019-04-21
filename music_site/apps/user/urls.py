from django.urls import path
from .views import *


urlpatterns = [
    # 用户登录和注册
    path('login.html', LoginView, name='login'),
    # 用户中心
    path('home/<int:page>.html', HomeView, name='home'),
    # 退出用户登录
    path('logout.html', LogoutView, name='logout'),
]
