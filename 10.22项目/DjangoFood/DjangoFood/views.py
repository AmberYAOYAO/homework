from django.shortcuts import render_to_response,HttpResponse
from Foods.models import *
from django.shortcuts import render
import random,json

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_username = request.COOKIES.get("username")
        session_username = request.session.get("username")
        if cookie_username and session_username and cookie_username == session_username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner
@loginValid
def beef(request):
    news_list = News.objects.order_by("-time")[:8]
    return  render_to_response("beef-index.html",locals())





#添加商品类型
def add_food_type(request):
    type_list = ["经典牛排","意面/烩饭","风味披萨","甜品小食","酒水饮料","其他"]
    for types in type_list:
        t = Foods_type()
        t.label = types
        t.description = "%s好吃不贵"%types
        # t.save()
    return HttpResponse("类型保存成功")
# #添加商品
def add_foods(request):
    food_list = ["茶漱海鲜汤","玉米海螺沟","芝士蛋糕卷","芝士大虾","西冷牛排",
                 "草莓布丁杯","黑椒牛排","榴莲芒果塔"]
    for food in food_list:
        t = Foods()
        t.name = food
        t.price = random.randint(1,400)
        t.picture = '1.jpg'
        t.description = "%s好吃，且贵"%food
        t.type_id = Foods_type.objects.get(id=random.randint(1,6))
        # t.save()
    return HttpResponse("食品保存成功")

# #添加文章
def add_news(request):
    address = ['喀什','哈密','吐鲁番','阿克苏','和田','伊宁','塔城']
    for i in range(30):
        news = News()
        title = "贵族食代牛排%s餐厅开业"%random.choice(address)
        news.title = title
        news.time = "%s-%s-%s"%(
            random.randint(1990,2050),
            random.randint(1, 12),
            random.randint(1, 28)
        )
        news.description = title*10
        news.image = "1.jpg"
        news.content = title*20
        news.type = "新闻资讯"
        # news.save()
    return HttpResponse("新闻保存成功")
def add_shop(request):
    address = ["石河子",'喀什','哈密','吐鲁番','阿克苏','和田','伊宁','塔城']
    for i in range(30):
        shop = Shop()
        shop.name = "贵族食代牛排%s餐厅"%random.choice(address)
        shop.picture = "1.jpg"
        shop.open_time = "上午10:00-13:00 下午14:00-23:00"
        shop.stop_car = "付费停车，30元/平米/小时"
        shop.address = random.choice(address)
        shop.label = "法国菜,有包间,有车位,可刷卡,崇文区,地铁1号线,地铁2号线,地铁5号线,崇文门外大街,前门总医院,天坛,祈年殿,龙潭湖公园,北京体育馆,中央戏剧学院,崇文区儿童医院,新世界商场,北京站,新闻大厦,北京饭店,北京市政府,东交民巷,天安门,朋友聚会,家人就餐,谈情约会"
        # shop.save()
        for i in range(random.randint(6,9)):
            shop.foods_id.add(
                Foods.objects.get(id=random.randint(1,9))
            )
            # shop.save()
    return HttpResponse("店铺保存成功")

# def beef(request):
#     news_list = News.objects.order_by("-time")[:8]
#     return  render_to_response("beef-index.html",locals())

def shop(request):
    shop_list = Shop.objects.all()
    return render_to_response("shop.html",locals())

def shop_con(request,id):
    shop = Shop.objects.get(id=int(id))
    foods_list = shop.foods_id.all()#多对多查询
    return render_to_response("shop-con.html",locals())

def news_con(request,id):
    news=News.objects.get(id=int(id))
    return render_to_response("news-con.html",locals())


def requestExample(request):
    # methods = dir(request)
    # username = request.GET.get("u")
    # username = request.GET.get("g")
    # username = request.GET.get("p")
    # foods_list = []
    # d = request.GET.get("d") #获取前端提交的name为d的数据
    # if d:
    #     foods_list = Foods.objects.filter(name__contains=d) #进行模糊查询
    food_type_list = Foods_type.objects.values("id","label").all()
    if request.method == "POST":
        #接收数据
        args = request.POST
        name = args.get("name")
        price = args.get("price")
        description = args.get("description")
        type_id = args.get("type_id")
        picture = request.FILES.get("picture")#文件需要用request.FILES接收
        #保存数据
        food = Foods()
        food.name = name
        food.price = price
        food.description = description
        food.type_id = Foods_type.objects.get(id=int(type_id))
        food.picture = picture
        food.save()
    return render(request,"test_request.html",locals())

from django.http import JsonResponse
def find_food(request):
    food_name = request.GET.get("food_name")
    food_data = []
    if food_name:
        food_list = Foods.objects.filter(name__contains=food_name)
        for f in food_list:
            food_data.append({"name":f.name})
    return JsonResponse({"food_data":food_data})



def ajax_get_page(request):
    return render(request,"ajax_get_page.html")

def ajax_get_data(request):
    html = "<span style='color:red;'>牛</span>"
    shop_list = [{"name":shop.name.replace("牛",html)} for shop in Shop.objects.all()]
    return JsonResponse({"shop_list":shop_list})


def ajax_post_page(request):
    return render(request,"ajax_post_page.html")
def ajax_post_data(request):
    result = ""
    if request.method == "POST":
        name = request.POST.get("name")
        result = "知道了，你是%s"%name
    return JsonResponse({"result":result})

def form_check(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            pass
        else:
            error = "用户名和密码不可以为空"
    return render(request,"form_check.html")

from Foods.forms import *

def p_form(request):
    userform = UserForm()
    foodform = FoodsForm()
    if request.method == "POST":
        form_data = FoodsForm(request.POST,request.FILES)#将提交的数据交给form表单进行校验
        if form_data.is_valid():
            request_data = form_data.cleaned_data#获取校验后的数据
            print(request_data)
            food = Foods()
            food.name = request_data.get("name")
            food.price = request_data.get("price")
            food.picture = request_data.get("picture")
            food.description = request_data.get("description")
            type_id = request_data.get("type_id")
            food. type_id =  type_id
            food.save()
        else:
            errors = form_data.errors #错误集中在这个方法里面
    return render(request,"python_forms.html",locals())

# from django.core.paginator import Paginator
# def news(request,page):
#     cookie_username = request.COOKIES.get("username")
#     article_list = News.objects.order_by("-time")
#     page_obj = Paginator(article_list,5)
#     page_data = page_obj.page(int(page))
#     #page_range = page_obj.page_range #页面范围
#     return render(request,"news.html",locals())

def setCookie(request):
    response = render(request,"beef-index.html")
    response.set_cookie("username","Tom")
    response.set_cookie("age","2")
    return response

def del_cookie(request):
    response = render(request,"beef-index.html")
    response.delete_cookie("age")
    return response


import hashlib
def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User()
        user.username = username
        user.password = set_password(password)
        user.save()
    return render(request,"register.html",locals())

# def beef(request):
#     #获取cookie
#     cookie_username = request.COOKIES.get("username")
#     session_username = request.session.get("username")
#     if cookie_username and session_username and cookie_username == session_username:
#        #如果cookie存在，就登录首页，这里的判断可以按照自己的思路肆意更改
#         news_list = News.objects.order_by("-time")[:8]
#         return render(request,"beef-index.html",locals())
#     else:
#         #否则就返回登录页
#         return HttpResponseRedirect("/login/")

from django.http import HttpResponseRedirect
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #通过查询判断用户名是否存在
        user = User.objects.filter(username=username).first()
        if user:
            #将请求携带的密码进行加密，进行比对
            post_password = set_password(password)
            if user.password == post_password:
                #密码正确设置cookie
                response = HttpResponseRedirect("/beef/")
                response.set_cookie("username",user.username)
                request.session["username"] = user.username
                #返回响应
                return response
    return render(request,"login.html")

def logout(request):
     response = HttpResponseRedirect("/login/")
     response.delete_cookie("username")
     del request.session["username"]
     return response

def vueExample(request):
    return render(request,"vueExample.html",locals())

from django.views import View
class FoodView(View):
    def __init__(self,**kwargs):
        super(FoodView,self).__init__()
        self.result={
            "version":"v1.0",
            "code":200,
            "data":[]
        }
    def is_exit(self,id):
        try:
            data=Foods.objects.get(id=id)
        except Exception as e:
            self.result["code"] = 500
            self.result["data"].append(str(e))
            return False
        else:
            return data
    def one_data(self,data):
        d = {"name": data.name, "price":
            data.price, "picture": data.picture.url,
             "description": data.description,
             "type": data.type_id.label}
        self.result["data"].append(d)
    def get(self,request):
        id = request.GET.get("id")
        #如果get请求传递id，返回id对应的数据
        #json格式无法封装python数据对象，所以要做数据转义
        if id:
           data = self.is_exit("id")
           if data:
               self.one_data(data)
                #如果没有id返回所有数据
        else:
            data = [{"name":data.name,"price":
                data.price,"picture":data.picture.url,
                "description":data.description,
                "type":data.type_id.label}for data in
                    Foods.objects.all()]
            self.result["data"] = data
        return JsonResponse(self.result)

    def post(self,request):
        post_data = request.POST
        name = post_data.get("name")
        price = post_data.get("price")
        picture = post_data.get("picture")
        description = post_data.get("description")
        type_id = post_data.get("type_id")

        foods = Foods()
        foods.name = name
        foods.price = price
        foods.picture = picture
        foods.description = description
        foods.type_id = Foods_type.objects.get(id=int(type_id))
        foods.save()
        self.one_data(foods)
        return JsonResponse(self.result)

    def put(self,request):
        put_data = json.loads(request.body.decode())

        id = put_data.get("id")
        name = put_data.get("name")
        price = put_data.get("price")
        picture = put_data.get("picture")
        description = put_data.get("description")
        type_id = put_data.get("type_id")

        foods = self.is_exit(id)
        if foods:
            foods.name = name
            foods.price = price
            foods.picture = picture
            foods.description = description
            foods.type_id = Foods_type.objects.get(id=int(type_id))
            foods.save()
            self.one_data(foods)
        return JsonResponse(self.result)

    def delete(self,request):
        delete_data = json.loads(request.body.decode())
        id = delete_data.get("id")

        foods = self.is_exit(id)
        if foods:
            d={
                "name":foods.name,
                "price":foods.price,
                "picture":foods.picture.url,
                "description":foods.description,
                "type":foods.type_id.label
            }
            self.result["data"].append(d)
            foods.delete()
        return JsonResponse(self.result)

from Foods.models import Foods
from Foods.serializers import FoodSerializers
from rest_framework import mixins,viewsets

class Foods_View(mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = Foods.objects.all()[:6]
    serializer_class = FoodSerializers



def ajax_vue(request):
    return render(request,'ajax_vue.html',locals())

def meishi(request):
    return render(request,"meishi.html",locals())