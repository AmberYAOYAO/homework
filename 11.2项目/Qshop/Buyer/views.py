from django.http import HttpResponseRedirect
from django.shortcuts import render
from Quser.models import Quser
from Quser.views import valid_user, set_password, add_user
from Shop.models import *
def index(request):
    #查询所有类型
    type_list = GoodsType.objects.all()[:3]
    #查询单个类型
    # type_data = GoodsType.objects.get(id=1)
    #查询对应类型的所有商品
    # type_data.goods_set.all()
    #查询每个类型对应的4个商品
    # for t in type_list:
    #     goods_list = t.goods_set.all()[:4]
    #上述内容进行整理
    # result = [{t.name:t.goods_set.all(),"pic":t.picture} for t in type_list]
    message = "favourite"
    return render(request,"buyer/index.html",locals())

def login_valid(fun):
    def inner(request,*args,**kwargs):
        referer = request.GET.get("referer")#证明使用者的目的地在购物车页面
        cookie_user = request.COOKIES.get("email")
        session_user = request.session.get("email")
        if cookie_user and session_user and cookie_user == session_user:
            return fun(request,*args,**kwargs)
        else:
            login_url = "/Buyer/login/"
            if referer:
                login_url = "/Buyer/login/?referer=%s"%referer
            return HttpResponseRedirect(login_url)

    return inner

def register(request):
    """
    前台买家注册功能
    :param request:
    :return:
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
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
            return HttpResponseRedirect("/Buyer/login/")
    return render(request,"buyer/register.html",locals())

def login(request):
    """
    记录登录请求是从哪到的登录页面
    :param request:
    :return:
    """
    referer = request.GET.get("referer")
    if not referer:
        referer = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        #判断用户是否存在
        #如果存在
        user = valid_user(email)
        if user:
            #判断密码是否正确
            db_password = user.password
            request_password = set_password(password)
            if db_password == request_password:
                if request.POST.get("referer"):
                    referer = request.POST.get("referer")
                if referer in ('http://127.0.0.1:8000/Buyer/login/',"None"):
                    referer = "/"
                response = HttpResponseRedirect(referer)
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",user.id)
                response.set_cookie("picture",user.picture)
                request.session["email"] = user.email
                return response
            else:
                error = "密码错误"
        else:
            error = "用户不存在"
    return render(request,"buyer/login.html",locals())

@login_valid
def cart(request):
    return render(request,"buyer/cart.html")

def place_order(request):
    return render(request,"buyer/place_order.html")

import time
from Buyer.pay import Pay
def get_pay(request):
    order_number = str(time.time()).replace(".","")
    order_price = "666.66"
    url = Pay(order_number,order_price)
    return HttpResponseRedirect(url)
def pay_result(request):
    data = request.GET
    return render(request,"buyer/pay_result.html",locals())
def goods_list(request):
    id = request.GET.get("id")
    goods_list = Goods.objects.all()
    if id:
        goods_type = GoodsType.objects.get(id=int(id))
        goods_list = goods_type.goods_set.filter(statue=1)
    return render(request,"buyer/goods_list.html",{"goods_list":goods_list})

def goods(request,id):
    goods_data = Goods.objects.get(id=int(id))
    return render(request,"buyer/goods.html",locals())

def logout(request):
    """
    后台卖家退出登录功能
    :param request:
    :return:
    """
    response = HttpResponseRedirect("/Buyer/login/")
    response.delete_cookie("email")
    response.delete_cookie("user_id")
    request.session.clear()
    return response

def user_site(request):
    return render(request,"buyer/user_center_site.html")

def user_order(request):
    return render(request,"buyer/user_center_order.html")

def user_info(request):
    return render(request,"buyer/user_center_info.html")
# Create your views here.
