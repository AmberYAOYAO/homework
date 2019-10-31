from django.shortcuts import render
from Shop.models import *
def index(request):
    shouye = Goods.objects.all()
    #查询所有类型
    type_list = GoodsType.objects.all()[:3]
    #查询单个类型
    type_data = GoodsType.objects.get(id=1)
    #查询对应类型的所有商品
    type_data.goods_set.all()
    #查询每个类型对应的4个商品
    for t in type_list:
        goods_list = t.goods_set.all()[:4]
    #上述内容进行整理
    result = [{t.name:t.goods_set.all(),"pic":t.picture} for t in type_list]
    message = "fruit"
    return render(request,"buyer/index.html",locals())

def goods_list(request):
    id = request.GET.get("id")
    goods_list = Goods.objects.all()
    if id:
        goods_type = GoodsType.objects.get(id=int(id))
        goods_list = goods_type.goods_set.all()
    return render(request,"buyer/goods_list.html",{"goods_list":goods_list})

def goods(request,id):
    goods_data = Goods.objects.get(id=int(id))
    return render(request,"buyer/goods.html",locals())
# Create your views here.
