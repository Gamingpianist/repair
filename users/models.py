from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    username = models.CharField(max_length=20, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=20, verbose_name='密码')
    name = models.CharField(max_length=10, verbose_name='姓名')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), verbose_name='性别')
    phone = models.CharField(max_length=15, verbose_name='联系方式')

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

