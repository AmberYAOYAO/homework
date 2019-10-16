from django.shortcuts import render_to_response
from News.models import News
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