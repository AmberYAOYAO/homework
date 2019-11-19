from flask import Flask
import datetime
#实例化flask服务
app = Flask(__name__)
#同时可以配置静态文件和模板文件目录
#默认静态文件的目录，在当前文件的同目录下的static目录下 配置项static_folder
#默认模板文件的目录，在当前文件的同目录下的templates目录下 配置项template_folder

#使用装饰器来确定路由
@app.route("/")
def index():
    return "hello world"

@app.route("/hello")
def hello():
    return "<h1>hello world</h1>"

@app.route("/self/<name>")
def my_self(name):
    return "<h1>hello world,I am %s</h1>"%name

@app.route("/self1/<int:name>")
def my_self1(name):
    return "<h1>hello world1,I am %s</h1>"%name

@app.route("/self2/<string:name>")
def my_self2(name):
    return "<h1>hello world2,I am %s</h1>"%name

@app.route("/self3/<float:name>")
def my_self3(name):
    return "<h1>hello world3,I am %s</h1>"%name

@app.route("/self4/<path:name>")
def my_self4(name):
    return "<h1>hello world4,I am %s</h1>"%name

@app.route("/birthday/<int:year>/<int:month>/<int:day>")
def birthday(year,month,day):
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    #date=datetime.datetime(year,month,day).strftime("%j")
    return "<h1>你的生日是{}年{}月的{}日,这是今年的第{}天</h1>".format(year,month,day,((date1-date2).days+1))

from flask import render_template
@app.route("/index/")
def index_page():
    a = 1
    b = 2
    c = 3
    d = "ddddaddaddd"
    e = range(10)
    site = "www.baidu.com"
    return render_template("index.html", **locals())

def get_upper(obj):
    return obj.upper()

app.add_template_filter(get_upper,"site")

def list():
    return render_template("list.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8000,debug=False,use_reloader=True)