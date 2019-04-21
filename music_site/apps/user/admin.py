from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserInfo
# Register your models here.


@admin.register(UserInfo)
class UserInfoAdmin(UserAdmin):
    list_display = ('username', 'email', 'mobile', 'qq', 'WeChat')
    # 将源码的UserAdmin.fieldsets转换为列表格式
    fieldsets = list(UserAdmin.fieldsets)
    # 重写UserAdmin.fieldsets，添加'mobile', 'qq', 'WeChat'展示在用户页面
    fieldsets[1] = (_('Personal info'), 
                    {'fields': ('first_name', 'last_name', 'email', 'mobile', 'qq', 'WeChat')})
