from django.http import HttpResponse
import random
# from django.shortcuts import render
import time
date1=time.localtime()
date2=time.mktime(date1)
def index(request):
    return HttpResponse('hello world!')
def say_hello(request):
    return HttpResponse('<h1 style=color:red>hello world I am dhx</h1>')
def demo(request):
    s='<table border="1">'
    # for row in range(1,10):
    #     if row%2==0:
    #         s+='<tr style="background:purple">'
    #     else:
    #         s+='<tr style="background:orange">'
    #     for col in range(1,row+1):
    #         s+='<td>'+str(row)+'*'+str(col)+'='+str(row*col)+'</td>'
    #     s+='</tr>'
    for row in range(1, 10):
        r = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        s += '<tr style="background:rgb('+str(r)+','+str(g)+','+str(b)+')">'
        for col in range(1, row + 1):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            s += '<td style="background:rgb('+str(r)+','+str(g)+','+str(b)+')" >' + str(row) +'*'+ str(col) + '=' + str(row * col) + '</td>'
        s += '</tr>'
    s+='</table>'

    return HttpResponse(s)
    # return HttpResponse('<h1 style=color:blue>list1=["%d*%d=%d"%(x,y,x*y)for x in range(1,10)for y in range(1,x+1)]</h1>')
    # result = '<h1 style=color:blue>%s*%s=%s%(row,col,row*col)</h1>'

def birthday(request,d1,d2):
    string="<h1 style='color:red';> 我的生日是%s,今年的生日是%s 现在的日期是%s，是2019年的第%s天</h1>"%(d1,d2,date1,date2)
    return HttpResponse(string)

def get_birthday(request,month,day):
    birth=time.mktime((2019,int(month),int(day),0,0,0,0,0,0))
    date=time.localtime(birth).tm_yday
    html="""
         <html>
             <head>
                 <title>
                 </title>
                 <style>
                     .content{
                        color:red;
                        text-align:center;
                     }
                 </style>
             </head>
             <body>
                 <h1 align='center'>算算你的生日是今年第几天</h1>
                 <p class='content'>%s</p>
             </body>
         </html>
    """
    new_day='你的生日是%s月%s日，是今年的第%s天'%(month,day,date)
    return HttpResponse(html%new_day)

from django.template.loader import get_template
def index1(request):
    """
    当前视图加载index.html，index.html的路径来源于settings配置文件里的TEMPLATES配置
    """
    template=get_template("index.html")#加载的步骤
    response=template.render({"name":"Tom","other_name":"Jerry"})#渲染
    return HttpResponse(response)#返回一个响应，响应的内容是一个渲染的结果
from django.shortcuts import render_to_response
class Example:
    age=1
    def say_hello(self):
        return ('hello word!')
def in_page(request):
    name="Tom"
    list_name=[1,2,3,4]
    tuple_name=(1,2,3,4)
    dict_name={"Jerry",1}
    fun_name=lambda x: x
    class_name=Example
    return render_to_response("index.html",locals())
def dog(request):
    dog_list=[
        {"name":"柴犬","price":"价格：100$","characteristic":"特征：强颜欢笑","url":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3068692520,868966390&fm=26&gp=0.jpg"},
        {"name": "杜宾", "price": "价格：100$", "characteristic": "特征：眼神杀","url":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2871131748,947105105&fm=26&gp=0.jpg"},
        {"name": "哈士奇", "price": "价格：100$", "characteristic": "特征：拆家","url":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=102637356,3902559687&fm=26&gp=0.jpg"},
        {"name": "萨摩耶", "price": "价格：100$", "characteristic": "特征：傻笑","url":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2977780713,3568347995&fm=26&gp=0.jpg"},
        {"name": "阿拉斯加", "price": "价格：100$", "characteristic": "特征：掉毛","url":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=188985851,1521292545&fm=26&gp=0.jpg"},
    ]
    return render_to_response("list.html", locals())
def shop(request):
    shop_list=[
        {"style":1,"name":"北京朝阳区店","url":"/static/img/shop-pic1.jpg","class":"shop-wrap shop-right"},
        {"style": 1, "name": "上海徐汇区区店", "url": "/static/img/shop-pic2.jpg", "class": "shop-wrap shop-right"},
        {"style": 2, "name": "厦门集美区店", "url": "/static/img/shop-pic3.jpg", "class": "shop-wrap"},
        {"style": 1, "name": "广州番禹区店", "url": "/static/img/shop-pic4.jpg", "class": "shop-wrap shop-right"},
        {"style": 1, "name": "深圳福田区店", "url": "/static/img/shop-pic5.jpg", "class": "shop-wrap shop-right"},
        {"style": 2, "name": "其他区店", "url": "/static/img/shop-pic6.jpg", "class": "shop-wrap"}
    ]
    return render_to_response("shop.html",locals())