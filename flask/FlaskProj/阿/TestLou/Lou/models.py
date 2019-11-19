from Lou import db


#定义数据库模型
class Model(db.Model):
    __abstract__ = True #代表当前类为抽象类，不会再继承过程当中执行
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        session = db.session()
        session.add(self)
        session.commit()

    def delete(self):
        session = db.session()
        session.delete(self)
        session.commit()

class User(Model):
    nick_name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))

class Label(Model):
    l_name = db.Column(db.String(32)) #标签名称
    description = db.Column(db.Text) #标签描述
    c_label = db.relationship("Course",backref="class_label")
    def __repr__(self):
        return self.l_name


class Course(Model):
    c_name = db.Column(db.String(32))
    description = db.Column(db.Text)
    picture = db.Column(db.String(32))
    show_number = db.Column(db.Integer)
    c_time_number = db.Column(db.Integer)
    state = db.Column(db.Integer,default = 1)#课程状态 0 即将上线  1上线 默认为1
    c_type = db.Column(db.Integer,default=0)#课程类型 0免费  1限时免费  2VIP会员  默认免费
    label_id = db.Column(db.Integer,db.ForeignKey("label.id"))
    def __repr__(self):
        return self.c_name

    # def __repr__(self):
    #     return str([self.c_name,self.description])


# class Role(Model):
#     r_name = db.Column(db.Text)
#     description = db.Column(db.Text)
#     user_role = db.relationship("User",backref = "role")

#映射表 中间表
# user_course = db.Table(
#     'user_course',#表名
#     db.Column("id",db.Integer,primary_key=True,autoincrement=True),
#     db.Column("user_id",db.Integer,db.ForeignKey("user.id")),
#     db.Column("course_id",db.Integer,db.ForeignKey("course.id")))
#     #这种搭建方式，只用于关系表
# class User(Model):
#     u_name = db.Column(db.String(32))
#     u_password = db.Column(db.String(32))
#
#     role_id = db.Column(db.Integer,db.ForeignKey("role.id"))
#     course = db.relationship("Course",secondary = user_course,backref='c_user')
#     def __repr__(self):
#         return self.u_name


# class Course(Model):
#     c_name = db.Column(db.String(32))
#     description = db.Column(db.Text)
#
#     def __repr__(self):
#         return str([self.c_name,self.description])
# #同步数据库
# db.create_all()