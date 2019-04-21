from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import UserInfo
from .forms import UserInfoForm
from index.models import Dynamic

# Create your views here.


def LoginView(request):
    """用户注册与登录"""
    # GET方法
    user = UserInfoForm()
    # 表单提交，POST方法，登录
    if request.method == 'POST':
        # 判断表单提交是用户登录还是用户注册
        # 用户登录
        if request.POST.get('loginuser', ''):
            loginuser = request.POST.get('loginuser', '')
            password = request.POST.get('password', '')
            if UserInfo.objects.filter(Q(mobile=loginuser) | Q(username=loginuser)):
                user = UserInfo.objects.filter(Q(mobile=loginuser) | Q(username=loginuser)).first()
                if check_password(password, user.password):
                    login(request, user)
                    return redirect('/user/home/1.html')
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        else:
            user = UserInfoForm(request.POST, request=request)
            if user.is_valid():
                user.save()
                tips = '注册成功'
            else:
                if user.errors.get('username', ''):
                    tips = user.errors.get('username', '注册失败')
                else:
                    tips = user.errors.get('mobile', '注册失败')
    return render(request, 'login.html', locals())


@login_required(login_url='user:login')
def HomeView(request, page):
    # 搜索歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    # 分页功能
    song_info = request.session.get('play_list', '')
    paginator = Paginator(song_info, 3)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', locals())


def LogoutView(request):
    logout(request)
    return redirect('/')
