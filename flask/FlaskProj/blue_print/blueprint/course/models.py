from blueprint import db
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