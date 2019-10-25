from django.shortcuts import render
from django.http import HttpResponseRedirect
from Quser.views import *

def login_valid(fun):
    def inner(request,*args,**kwargs):
        cookie_user = request.COOKIES.get("email")
        session_user = request.session.get("email")
        if cookie_user and session_user and cookie_user == session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Shop/login/")

    return inner




def register(request):
    """
    后台卖家注册功能
    :param request:
    :return:
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #检测用户是否注册过
        #注册过,提示当前邮箱已经注册
        error = " "
        if valid_user(email):
           error = "当前邮箱已经注册"
        #没有注册过
        else:
            #对密码加密
            password = set_password(password)
            #保存到数据库
            add_user(email = email,password = password)
            #跳转到登录
            return HttpResponseRedirect("/Shop/login")
    return render(request,"shop/register.html",locals())


def login(request):
    """
    后台卖家登录功能
    :param request:
    :return:
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #判断用户是否存在
        #如果存在
        user = valid_user(email)
        if user:
            #判断密码是否正确
            db_password = user.password
            request_password = set_password(password)
            if db_password == request_password:
                response = HttpResponseRedirect("/Shop/")
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",user.id)
                request.session["email"] = user.email
                return response
            else:
                error = "密码错误"
        else:
            error = "用户不存在"
    return render(request,"shop/login.html",locals())

@login_valid
def index(request):
    """
    后台卖家首页
    :param request:
    :return:
    """
    return render(request,"shop/index.html")

def logout(request):
    """
    后台卖家退出登录功能
    :param request:
    :return:
    """
    response = HttpResponseRedirect("/Shop/login/")
    response.delete_cookie("email")
    response.delete_cookie("user_id")
    request.session.clear()
    return response


def forget_password(request):
    """
    后台卖家忘记密码功能
    :param request:
    :return:
    """
    return render(request,"shop/forgot-password.html")
# Create your views here.
