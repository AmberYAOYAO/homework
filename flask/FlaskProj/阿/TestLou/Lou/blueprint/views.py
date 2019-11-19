"""
视图文件
"""
import os
from Lou.blueprint import lou_app
from flask import render_template
from flask import request
from Lou.models import *
from sqlalchemy import or_,and_
from flask import redirect
from flask import Response
import hashlib
import functools

def loginValid(fun):
    @functools.wraps(fun) #保留原来的命名来区别被装饰后的函数
    def inner(*args,**kwargs):
        username = request.cookies.get("username")
        if username:
            return fun(*args,**kwargs)
        else:
            return redirect("/index/")
    return inner

def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

@lou_app.route("/",methods=["get","post"])
def index():
    register = request.args.get("register")
    if request.method == "POST":
        username = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User()
        user.nick_name = username
        user.password = set_password(password)
        user.email = email
        user.save()
        register = True
    response = Response(render_template("index.html", **locals()))
    return response

@lou_app.route("/login/",methods=["get","post"])
def login():
    response = redirect("/") #跳转回首页
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email = email).first()
        if user:
            request_password = set_password(password)
            if request_password == user.password:
                response.set_cookie("email", user.email)
    return response

@lou_app.route("/logout/")
def logout():
    response = redirect("/")
    response.delete_cookie("email")
    return response


@lou_app.route("/course/<path:url_arg>/")
@loginValid
def course(url_arg):
    #获取label，固定
    label_list = Label.query.all()
    #获取url上匹配的过滤条件，并且使用/对过滤条件进行切分
    args = url_arg.split("/")
    #测试过滤条件的长度
    len_arg = len(args)
    #如果参数的个数是两个，那么安装参数1是类型 参数2是标签进行查询
    #设置全局参数，防止在判断的时候有条件分支缺失导致变量不存在
    c_type = "" #url传递过来的课程类型
    label = ""  #url传递过来的课程标签
    referer_url = ""  #提供lable重新定位的参数
    referer_url1 = ""  #提供给c_type重新定位的参数
    if len_arg == 2: #请求由类型也有标签
        c_type,label = args #分解参数
        #查询python所有免费或者付费
        referer_url = "/course/%s/" % c_type #定义lable标签的链接
        referer_url1 = label + "/"  #定义课程类型的链接
        label_id = Label.query.filter_by(l_name = label)[0].id #获取对应的标签
        course_list = Course.query.filter(
            and_(
                Course.c_type == int(c_type),
                Course.label_id == label_id
            )
        )  # 查询所对应的多有课程
        if int(c_type) == 3:
            course_list = Course.query.filter(
                and_(
                    Course.label_id == label_id
                )
            ) #查询所对应的多有课程
    #url只有一个路由请求参数
    elif len_arg == 1:
        arg, = args #获取参数
        if arg.isdigit(): #通过类型判断参数是c_type 函数 lable
            c_type = arg #请求参数是c_type
            referer_url = "/course/%s/"%c_type #定义lable标签的链接
            if int(c_type) == 3: #判断全部
                course_list = Course.query.all()
            else:
                course_list = Course.query.filter_by(c_type=int(c_type))
        else:
            label = arg
            referer_url1 = label+"/" #定义c_type标签的链接
            course_list = Label.query.filter_by(l_name=label)[0].c_label
    print("c_type: %s"%c_type)
    print("label: %s"%label)
    return render_template("courses/course.html",**locals())

@lou_app.route("/course_show/")
def course_show():
    return render_template("courses/course_show.html")

@lou_app.route("/course_report/")
def course_report():
    return render_template("courses/course_report.html")


@lou_app.route("/get_test/",methods=["GET","POST"])
def get_test():
    course = ""
    label_list = Label.query.all()
    if request.method == "POST":
        data = request.form
        c_name = data.get("c_name")
        show_number = data.get("show_number")
        c_time_number = data.get("c_time_number")
        label = data.get("label")
        description = data.get("description")
        logo = request.files.get("logo")

        #保存文件分为两步
        # 文件保存到服务器
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "static\img\%s" % logo.filename
        )
        logo.save(file_path)
        #文件路径保存到数据中
        course = Course()
        course.c_name = c_name
        course.show_number = show_number
        course.description = description
        course.c_time_number = c_time_number
        course.picture = "img\%s" % logo.filename #保存图片路径
        course.class_label = Label.query.get(int(label)) #保存外键
        course.save()

    return render_template("request_example.html",**locals())

from Lou import api #来自init
from flask_restful import Resource

class CourseApi(Resource):
    def __init__(self):
        self.result = {
            "version": "v1",
            "code": "200",
            "data": [],
            "methods": "",
            "pageiation": {}
        }
        self.page_size = 15
    def to_dict(self,obj):
        query_str = str(obj.query).split("SELECT ")[1].split("FROM")[0].strip()
        key_list = [k.split(" AS ")[1].replace("course_","") for k in query_str.split(",")]
        obj_to_dict = dict(
            zip(key_list,[getattr(obj,key) for key in key_list])
        )
        return obj_to_dict
    def get(self,id=None,page=None,page_num=None,field = None,value = None):
        if id:
            course_list = Course.query.get(int(id))
            data = self.to_dict(course_list)
            self.result["data"].append(data)
        else:
            #如果启用分页
            if page == "page":
                page_obj = Course.query.order_by(db.desc("id")).paginate(int(page_num), self.page_size)  # 第一个参数是页码，第二个参数每页条数
                if field and str(value):
                    dicts = {field:value}
                    page_obj = Course.query.filter_by(**dicts).paginate(int(page_num), self.page_size)
                self.result["pageiation"]["has_next"] = page_obj.has_next
                self.result["pageiation"]["has_prev"] = page_obj.has_prev
                self.result["pageiation"]["next_num"] = page_obj.next_num
                self.result["pageiation"]["page"] = page_obj.page
                self.result["pageiation"]["pages"] = list(range(1,page_obj.pages+1))
                self.result["pageiation"]["per_page"] = page_obj.per_page
                self.result["pageiation"]["prev_num"] = page_obj.prev_num
                self.result["pageiation"]["total"] = page_obj.total
                course_list = page_obj.items
            else:
                #如果有过滤条件，就按照过滤条件查询否则返回所有数据
                if field and str(value):
                    dicts = {field:value}
                    course_list = Course.query.filter_by(**dicts).all()
                else:
                    course_list = Course.query.all()
            self.result["data"] = [self.to_dict(i) for i in  course_list]
        self.result["methods"] = request.method
        return self.result

    def post(self):
        self.result["methods"] = request.method
        return self.result

    def put(self,id):
        self.result["methods"] = request.method
        return self.result

    def delete(self,id):
        self.result["methods"] = request.method
        return self.result

api.add_resource(
    CourseApi,
    "/CourseApi/",
    "/CourseApi/<int:id>/",
    "/CourseApi/<string:field>/<string:value>/",
    "/CourseApi/<string:field>/<string:value>/<string:page>/<int:page_num>/",
    "/CourseApi/page/<string:page>/<int:page_num>/"
)
from Lou.blueprint.form import UserForm
@lou_app.route("/page_1/",methods=["GET","POST"])
def page_1():
    user = UserForm() #前端展示表单
    if request.method == "POST":
        user = UserForm(request.form) #将请求的数据传入表单类
        # print(user.data) #请求数据
        # print(user.errors) #错误
        # print(user.validate()) #校验的结果
        if user.validate(): #镜像校验，如果成功，进行数据保存
            post_data = user.data
            message = "保存数据库"
        else: #失败后，会通过校验实例返回错误
            message = user.errors
    return render_template("1.html",**locals())

@lou_app.route("/page_2/")
@lou_app.route("/page_2/<int:id>/")
def page_2(id=1):
    return "id is %s"%id







