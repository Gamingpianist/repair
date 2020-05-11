from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

from .models import UserProfile
# Create your views here.
def index(request):
    return render(request, 'index.html')

class LoginView(View):
    '''用户登录'''

    def get(self, request):
        return render(request, "signin.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = UserProfile.objects.get(username=username)

        if not check_password(password, user.password):
            return render(request, "signin.html")

        if user:
            login(request, user)
            print("user{} login!".format(user.get_username()))
            return render(request, "index.html")
        else:
            return render(request, "signin.html")


class RegisterView(View):
    '''用户注册'''

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # 从前端获取submit信息
        username = request.POST.get("username")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        password = request.POST.get("password")

        # 创建新的UserProfile对象
        user = UserProfile.objects.create(
            username=username, name=name, phone=phone, gender=gender, password=make_password(password))
        user.is_superuser = False  # 去除管理权限
        user.save()

        login(request, user)  # 登录

        return render(request, 'index.html')


def userLogout(request):
    '''退出登录'''

    logout(request)
    return render(request, "index.html")
