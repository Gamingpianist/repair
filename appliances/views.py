import json
import traceback

from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Appliance

# Create your views here.


def ApplianceListView(request):
    limit = 6
    appliances = Appliance.objects.all()
    paginator =Paginator(appliances, limit)
    page = request.GET.get('page')
    try:
        appliances = paginator.page(page)
    except PageNotAnInteger:
        appliances = paginator.page(1)
    except EmptyPage:
        appliances = paginator.page(paginator.num_pages)
    return render(request, "services.html", {"appliances": appliances})



def viewByID(request):
    '''根据id获取appliance'''

    if request.method == 'GET':
        appid = request.GET.get('app_id')
        appliance = Appliance.objects.get(id=appid)
        return render(request, 'service-detail.html', {'appliance': appliance})
    else:
        return traceback.print_exc()


def searchByName(request):
    '''根据名称获取appliances列表(模糊搜索)'''
    if request.method == 'GET':
        appname = request.GET.get('app_name')
        appliances = Appliance.objects.filter(name__icontains=appname)
        return render(request, 'services.html', {'appliances': appliances})
    else:
        return traceback.print_exc()

