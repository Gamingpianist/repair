from django.db import models
from orders.models import Appliance
from users.models import UserProfile
# Create your models here.


class FeedBack(models.Model):
    content = models.TextField(verbose_name='反馈内容')
    date = models.DateField(verbose_name='反馈时间', auto_now=True)
    appliance = models.ForeignKey(
        Appliance, on_delete=models.CASCADE, verbose_name='家电名称')
    feeder = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, verbose_name='用户名')

    class Meta:
        verbose_name = '用户反馈信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)
