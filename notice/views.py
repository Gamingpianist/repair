from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Notice
# Create your views here.

def NoticeListView(request):


    limit = 3
    notices = Notice.objects.all()
    paginator = Paginator(notices, limit)
    page = request.GET.get('page')
    try:
        notices = paginator.page(page)
    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)
    return render(request, "notice.html", {"notices": notices})



#class NoticeListView(View):
    #'''获取所有notice'''

    #def get(self, request):
        #notices = Notice.objects.all()
        #return render(request, 'notice.html', {'notices': notices})


class NoticeView(View):
    '''获取notice详情'''

    def get(self, request):

        notice_id = request.GET.get('notice_id')
        notice = Notice.objects.get(id=notice_id)
        return render(request, 'notice-detail.html', {'notice': notice})
