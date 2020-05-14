from django.shortcuts import render
from django.views.generic.base import View

from .models import Notice
# Create your views here.


class NoticeListView(View):
    '''获取所有notice'''

    def get(self, request):
        notices = Notice.objects.all()
        return render(request, 'notice.html', {'notices': notices})


class NoticeView(View):
    '''获取notice详情'''

    def get(self, request):
        notice_id = request.GET.get('notice_id')
        notice = Notice.objects.get(id=notice_id)
        return render(request, 'notice-detail.html', {'notice': notice})
