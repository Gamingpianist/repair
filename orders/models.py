from django.db import models
from appliances.models import Appliance
from users.models import UserProfile
# Create your models here.


class Order(models.Model):

    date = models.DateTimeField(verbose_name='下单日期', auto_now=True)
    status = models.CharField(max_length=10, choices=(
        ('0', '待付款'), ('1', '待维修'), ('2', '已完成')), verbose_name='订单状态', default=0)
    price = models.FloatField(verbose_name='维修价格', default=0)
    appliance = models.ForeignKey(
        Appliance, on_delete=models.CASCADE, verbose_name='家电名称')
    name = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, verbose_name='姓名')
    address = models.TextField(verbose_name='地址')
    content = models.TextField(verbose_name='问题描述')

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)
