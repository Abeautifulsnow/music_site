from django.shortcuts import render
from django.views.generic import ListView
from index.models import *

# Create your views here.


def RankingView(request):
    """歌曲排行"""
    # 搜索歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    # 歌曲分类列表,筛选出不同行
    All_list = Song.objects.values('song_type').distinct()
    # 获取歌曲列表信息
    song_type = request.GET.get('type', '')
    if song_type:
        song_info = Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by('-dynamic_plays').all()[:10]
    else:
        song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
    return render(request, 'ranking.html', locals())


class RankingList(ListView):
    """通用视图"""
    # context_object_name设置Html模版的某一个变量名称
    context_object_name = 'song_info'
    # 设定模板文件
    template_name = 'ranking.html'
    # 查询变量song_info的数据
    def get_queryset(self):
        # 获取请求参数
        song_type = self.request.GET.get('type', '')
        if song_type:
            song_info = Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by('-dynamic_plays').all()[:10]
        else:
            song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
        return song_info
    
    # 添加其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 搜索歌曲
        context['search_song'] = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
        # 所有歌曲分类
        context['All_list'] = Song.objects.values('song_type').distinct()
        return context