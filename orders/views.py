from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
import traceback
from .models import Order
from .models import Appliance
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def OrderListView(request):
    try:
        limit = 3
        order = Order.objects.filter(name=request.user)
        paginator =Paginator(order, limit)
        page = request.GET.get('page')
        try:
            order = paginator.page(page)
        except PageNotAnInteger:
            order = paginator.page(1)
        except EmptyPage:
            order = paginator.page(paginator.num_pages)
        return render(request, "order.html", {"order": order})
    except:
        return redirect(reverse("index"))






#class OrderListView(View):

    #def get(self, request):
        #order = Order.objects.filter(name=request.user)
        #return render(request, "order.html", {"order": order})





class OrderView(View):
    '''用户下单'''
    def get(self, request):
        '''根据id获取appliance'''
        try:
            appid = request.GET.get('app_id')
            appliance = Appliance.objects.get(id=appid)
            return render(request, 'order-add.html', {'appliance': appliance})
        except:
            return redirect(reverse("index"))


    def post(self, request):
        # 从前端获取submit信
        try:
            appliance_name = request.POST.get("appliance")
            appliance = Appliance.objects.get(name=appliance_name)


            address = request.POST.get('address')
            content = request.POST.get('content')

            # 创建新的Order对象
            order = Order.objects.create(
                appliance=appliance, name=request.user, address=address, content=content)
            order.save()
            order_list = Order.objects.filter(name=request.user)

            return render(request, 'order.html', {'order': order_list})
        except:
            return redirect(reverse("index"))

def search(request):
    '''根据名称获取appliances列表(模糊搜索)'''
    try:
        if request.method == 'GET':

            appname = request.GET.get('app_name')
            appliance = Appliance.objects.get(name__icontains=appname)
            order = Order.objects.filter(appliance=appliance, name=request.user)
            return render(request, 'order.html', {'order': order})
    except:
        return redirect(reverse("index"))

class OrdersubView(View):
    def get(self, request):
        try:
            orderid = request.GET.get('order_id')
            order = Order.objects.get(id=orderid)
            return render(request, 'order-detail.html', {'order': order})
        except:
            return redirect(reverse("index"))


    def post(self, request):
        try:

            orderid = request.POST.get("order_id")
            order = Order.objects.get(id=orderid)
            order.status = "1"
            order.save()
            order_list = Order.objects.filter(name=request.user)

            return render(request, 'order.html', {'order': order_list})
        except:
            return redirect(reverse("index"))


def delete_order(request):
    try:
        delete_order = request.POST.get("order_id")
        Order.objects.get(id=delete_order).delete()
        order_list = Order.objects.filter(name=request.user)
        return render(request, 'order.html', {'order':order_list})
    except:
        return redirect(reverse("index"))




