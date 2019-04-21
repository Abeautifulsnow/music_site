from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
    qq = models.CharField('QQ号码', max_length=20)
    WeChat = models.CharField('微信账号', max_length=20)
    mobile = models.CharField('手机号码', max_length=11, unique=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username
