import json
import traceback

from django.shortcuts import render
from django.views.generic.base import View

from .models import Appliance

# Create your views here.


class ApplianceListView(View):
    '''获取全部appliance列表'''

    def get(self, request):
        appliances = Appliance.objects.all()
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

