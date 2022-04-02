from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from appliances.models import Appliance
from .models import UserProfile


# Create your views here.


def index(request):
    appliances = Appliance.objects.all()
    #print(appliances)
    return render(request, 'index.html', {'appliances': appliances})


def gallery(request):
    return render(request, 'gallery.html')


class LoginView(View):
    '''用户登录'''

    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return render(request, 'signin.html', {'content': '用户不存在'})

        if not check_password(password, user.password):
            return render(request, 'signin.html')

        login(request, user)
        #print('user{} login!'.format(user.get_username()))
        return redirect(reverse('index'))


class RegisterView(View):
    '''用户注册'''

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # 从前端获取submit信
        username = request.POST.get('username')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # 创建新的UserProfile对象
        try:
            user = UserProfile.objects.create(
                username=username, name=name, phone=phone, password=make_password(password))
        except:
            return render(request, 'signup.html', {'content': '用户名已存在!'})

        user.is_superuser = False  # 去除管理权限
        user.save()

        login(request, user)  # 登录

        return redirect(reverse('index'))


class UpdateView(View):
    '''变更用户信息'''

    def get(self, request):
        return render(request, 'userupdate.html')

    def post(self, request):
        user = request.user

        if user.is_superuser:
            return render(request, 'index.html', {'user': user})

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if name:
            user.name = name

        if phone:
            user.phone = phone

        if password:
            user.password = make_password(password)

        user.save()

        return render(request, 'index.html', {'user': user})


def user_logout(request):
    '''退出登录'''

    logout(request)
    return redirect(reverse('index'))
