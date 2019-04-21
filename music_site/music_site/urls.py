"""music_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from music_site.settings import MEDIA_ROOT, STATIC_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('user/', include('user.urls')),
    path('search/', include('search.urls')),
    path('ranking.html', include('ranking.urls')),
    path('play/', include('play.urls')),
    path('comment/', include('comment.urls')),
    # MEDIA路径,使用的时候请from music_site.settings import STATIC_ROOT
    re_path('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}, name='media'),
    # static路径
    re_path('^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}, name='static'),
]

# 或者这种方法
# from django.conf.urls.static import static
# from music_site.settings import MEDIA_URL, MEDIA_ROOT
# urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

# 设置404，500错误状态码
from index import views
handler404 = views.page_not_found
handler500 = views.page_not_found