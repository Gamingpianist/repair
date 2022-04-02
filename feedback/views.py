from django.shortcuts import render
from django.views.generic.base import View


from .models import FeedBack
# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from .models import FeedBack
from .models import Appliance
import traceback
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def FeedBackListView(request):
    try:
        limit = 3
        feedback_list = FeedBack.objects.filter(feeder=request.user)
        paginator =Paginator(feedback_list, limit)
        page = request.GET.get('page')
        try:
            feedback_list = paginator.page(page)
        except PageNotAnInteger:
            feedback_list = paginator.page(1)
        except EmptyPage:
            feedback_list = paginator.page(paginator.num_pages)
        return render(request, "feedback.html", {"feedback": feedback_list})
    except:
        return redirect(reverse("index"))

#class FeedBackListView(View):

    #def get(self, request):
        #feedback_list = FeedBack.objects.filter(feeder=request.user)
        #return render(request, 'feedback.html', {'feedback': feedback_list})

class FeedView(View):
    def get(self, request):
        try:
            applianceid = request.GET.get('appliance_id')
            appliance = Appliance.objects.get(id=applianceid)
            return render(request, 'feedback-add.html', {'appliance': appliance})
        except:
            return redirect(reverse("index"))

    def post(self, request):
        try:
            appliance_name = request.POST.get("appliance")
            appliance = Appliance.objects.get(name=appliance_name)
            content = request.POST.get('content')

            # 创建新的Order对象
            feedback = FeedBack.objects.create(
                appliance=appliance, feeder=request.user, content=content)
            feedback.save()
            feedback_list = FeedBack.objects.filter(feeder=request.user)

            return render(request, 'feedback.html', {'feedback': feedback_list})
        except:
            return redirect(reverse("index"))

def searchfor(request):
    '''根据名称获取appliances列表(模糊搜索)'''
    try:
        if request.method == 'GET':
            appname = request.GET.get('app_name')
            appliance = Appliance.objects.get(name__icontains=appname)
            feedback = FeedBack.objects.filter(appliance=appliance, feeder=request.user)
            return render(request, 'feedback.html', {'feedback': feedback})
    except:
        return redirect(reverse("index"))


class FeedbacksubView(View):
    def get(self, request):
        try:
            feedbackid = request.GET.get('feedback_id')
            feedback = FeedBack.objects.get(id=feedbackid)
            return render(request, 'feedback-detail.html', {'feedback': feedback})
        except:
            return redirect(reverse("index"))



def delete_feedback(request):
    try:
        delete_feedback = request.POST.get("feedback_id")
        FeedBack.objects.get(id=delete_feedback).delete()
        feedback_list = FeedBack.objects.filter(feeder=request.user)
        return render(request, 'feedback.html', {'feedback': feedback_list})
    except:
        return redirect(reverse("index"))