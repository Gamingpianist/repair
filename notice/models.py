from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    date = models.DateTimeField(verbose_name='公告日期')
    content = models.TextField(max_length='500', verbose_name='内容')

    class Meta:
        verbose_name = '公告信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title