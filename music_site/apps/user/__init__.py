import os
from django.apps import AppConfig


default_app_config = 'user.apps.UserConfig'

# 获取当前app名称
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

# 重写类UserConfig
class UserConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '用户'