from django.db import models

# Create your models here

class Appliance(models.Model):
    name = models.CharField(max_length=10, verbose_name='家电名称')
    description = models.TextField(verbose_name='家电描述')
    image = models.ImageField(upload_to='images', verbose_name='家电图片')

    class Meta:
        verbose_name = '维修家电信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name