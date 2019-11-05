from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from Quser.models import Quser
from Quser.views import valid_user, set_password, add_user
from Shop.models import *
from Buyer.models import *


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
    email = request.COOKIES.get("email")#获取用户邮箱
    goods_list = BuyCar.objects.filter(car_user=email)#获取用户邮箱对应的购物车数据
    count = len(goods_list)
    if request.method == "POST": #为了接收提交订单
        #对订单的处理
        data = request.POST
        post_data = []
        #过滤所有选择的商品的id和购买数量
        for key in data:
            if key.startswith("check"):
                id = key.split("_")[1]
                num = "number_%s"%id
                number = data[num]
                post_data.append((id,number))
        #保存订单主表
        p_order = Pay_order()
        p_order.order_id = str(time.time()).replace(".","")
        p_order.order_number = len(post_data)
        p_order.order_user = Quser.objects.get(email=request.COOKIES.get("email"))
        p_order.save()#这里没有保存总价

        order_total = 0 #总价计算
        #循环保存当前订单对应的订单详情
        for id,number in post_data:
            number = int(number)
            goods = Goods.objects.get(id=int(id))
            o_info = Order_info()
            o_info.order_id = p_order
            o_info.goods_name = goods.name
            o_info.goods_number = number
            o_info.goods_price = goods.price
            o_info.goods_total = number * goods.price
            o_info.goods_picture = goods.picture.url
            o_info.order_store = goods.goods_store
            o_info.save()
            order_total += o_info.goods_total
        p_order.order_total = order_total#保存当前订单的总价
        p_order.save()
        return HttpResponseRedirect("/Buyer/place_order/?order_id=%s"%p_order.order_id)

    return render(request,"buyer/cart.html",locals())

def place_order(request):
    order_id = request.GET.get("order_id")
    email = request.COOKIES.get("email")
    user = Quser.objects.get(email=email)
    addr = user.goodsaddress_set.filter()
    if order_id:
        p_order =Pay_order.objects.get(order_id=order_id)#订单信息
        order_info = p_order.order_info_set.all()#详情信息
    return render(request,"buyer/place_order.html",locals())

import time
from Buyer.pay import Pay
def get_pay(request):
    order_number = request.GET.get("order_id")
    order_price = request.GET.get("order_total")
    url = Pay(order_number,order_price)
    return HttpResponseRedirect(url)
def pay_result(request):
    data = request.GET
    order_id = request.GET.get(("out_trade_no"))
    p_order = Pay_order.objects.get(order_id=order_id)
    p_order.order_state = 1
    p_order.save()
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
    email = request.COOKIES.get("email")
    if email:
        now_data = History.objects.filter(user_email=email).order_by("id")
        if len(now_data) >= 5:
            now_data[0].delete()
        history = History()
        history.user_email = email
        history.goods_id = id
        history.goods_name = goods_data.name
        history.goods_price = goods_data.price
        history.goods_picture = goods_data.picture
        history.save()
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
from Quser.models import GoodsAddress
def user_site(request):
    email = request.COOKIES.get("email")
    user = Quser.objects.get(email=email)
    addr = user.goodsaddress_set.filter(state=1)[0]
    if request.method == "POST":
        receiver = request.POST.get("receiver")
        address = request.POST.get("address")
        postcode = request.POST.get("postcode")
        phone = request.POST.get("phone")

        addr = GoodsAddress()
        addr.receiver = receiver
        addr.address = address
        addr.postcode = postcode
        addr.phone = phone
        addr.state = 0
        addr.user = user
        addr.save()
    return render(request,"buyer/user_center_site.html",locals())

def user_order(request):
    return render(request,"buyer/user_center_order.html")

def user_center_info(request):
    user_email = request.COOKIES.get("email")#获取cookie当中的email
    user = Quser.objects.get(email = user_email) #获取用户信息
    goods_list = History.objects.filter(user_email=user_email)#获取历史记录
    return render(request,"buyer/user_center_info.html",locals())



def add_car(request):
    result = {"state":"error","data":""}
    if request.method == "POST":
        user = request.COOKIES.get("email")
        goods_id = request.POST.get("goods_id")
        number = request.POST.get("number",1)
        try:
            goods = Goods.objects.get(id = goods_id)
        except Exception as e:
            result["data"] = str(e)
        else:
            car = BuyCar()
            car.car_user = user
            car.goods_id = goods.id
            car.goods_name = goods.name
            car.goods_picture = goods.picture
            car.goods_price = goods.price
            car.goods_number = number
            car.goods_total = int(number)*goods.price
            car.goods_store = goods.goods_store.id
            car.save()
            result["state"] = "success"
            result["data"] = "加入购物车成功"
    return JsonResponse(result)
# Create your views here.
