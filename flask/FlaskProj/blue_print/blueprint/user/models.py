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

class User(Model):
    nick_name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))