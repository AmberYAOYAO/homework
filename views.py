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