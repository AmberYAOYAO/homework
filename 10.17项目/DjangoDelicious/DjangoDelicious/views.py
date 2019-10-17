from django.shortcuts import render_to_response
from django.http import HttpResponse
from News.models import *
from django.db.models import Max,Min,Count,Sum,Avg,F,Q
def beef(request):
    news_list = News.objects.all()#查询所有数据
    return render_to_response("beef-index.html",locals())
def news_con(request,id):
    news = News.objects.get(id=int(id))
    return render_to_response("news-con.html",locals())
def food(request):
    return render_to_response("meishi.html",locals())

def include_base(request):
    return render_to_response("include_base.html",locals())
#
# def add_type(request):
#     news_type = NewsType() #实例化orm对象
#     news_type.label = "宋词"
#     news_type.description= "如梦令"
#     news_type.save() #保存映射数据
#     return HttpResponse("save successfully")
#
# def add_News(request):
#     news = News() #实例化ORM对象
#     news.title="鬼灭之刃"
#     news.time = "2019-10-17"
#     news.description = "灶门祢豆子"
#     news.image = "2.jpg"
#     news.content = "看给孩子饿的"
#     news.type_id = NewsType.objects.get(id=2)
#     news.save()
#     news.editor_id.add(
#         Editor.objects.get(id=3)
#     )
#     news.save()
#     return  HttpResponse("save successfully")
def selectExample(request):
    # news = News.objects.get(id=1)#获取单条数据
    # news = News.objects.filter(title="鬼灭之刃",time="2019-10-16").first()
    # news2 = News.objects.filter(title="鬼灭之刃").last()#单条数据
    # news_list = News.objects.filter(id__lt=3)
    # news_list = News.objects.filter(id__lte=4)
    # news_list = News.objects.filter(id__gt=4)
    # news_list = News.objects.filter(id__gte=1)
    # news_list = News.objects.filter(id__in=[4,3,2,1])
    # news_list = News.objects.filter(title__contains="鬼")
    # news_list = News.objects.order_by("id")
    # news_list = News.objects.order_by("-id")
    # news_list = News.objects.order_by("id")[:2]
    # news_list = News.objects.order_by("-id")[:2]
    # news_list = NewsType.objects.get(id=1).news_set.all()
    #查询当前所有类型文章(外键查询)
    #------------
    #多对多查询
    # 查询一个编辑的所有新闻
    # news_list = NewsType.objects.get(id=1).news_set.all()
    #查询一个编辑的所有新闻
    # editor_list = News.objects.get(id=1).editor_id.all()
    #*****************
    #删
    # news=News.objects.get(id=8)
    # news.delete()
    #改
    # news=News.objects.get(id=7)
    # news.time="2019-10-18"
    # news.save()
    # news=News.objects.all()
    # news.update(content="") #只能修改多条和全部
    #@@@@@@@@@@@
    #聚类查询
    # news=News.objects.values("title").all()
    # news1=News.objects.all().aggregate(id_avg=Avg("id"),id_count=Count("id")
    #                                   ,id_sum=Sum("id"),id_max=Max("id"),
    #                                   id_min=Min("id"))
    #分组
    #查询所有文章标题出现的次数
    # news1 = News.objects.values('title').annotate(Count("title"))
    #查询以title分组，每组数据中最大的id
    # news1 = News.objects.values("title").annotate(Max("id"))
    #F查询  是以字段为条件的查询(必须是一张表的两个字段互相比较)
    # money_list = Money.objects.filter(money1__lt=F("money2")
    #Q查询
    # news = News.objects.filter(title="鬼灭之刃",id=6) #and
    # news=News.objects.filter(Q(title="海贼王")|Q(id=6))#or
    return render_to_response("selectpage.html",locals())
