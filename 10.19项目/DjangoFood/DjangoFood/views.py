from django.shortcuts import render_to_response,HttpResponse
from Food.models import *
from django.shortcuts import render
import random

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

def beef(request):
    news_list = News.objects.order_by("-time")[:8]
    return  render_to_response("beef-index.html",locals())

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

from Food.forms import *

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

from django.core.paginator import Paginator
def news(request,page):
    article_list = News.objects.order_by("-time")
    page_obj = Paginator(article_list,5)
    page_data = page_obj.page(int(page))
    #page_range = page_obj.page_range #页面范围
    return render(request,"news.html",locals())
