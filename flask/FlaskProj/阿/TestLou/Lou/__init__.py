"""
包实例化文件
"""
# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Api
# app = Flask(__name__)
# api = Api(app)
#
# base_path = os.path.abspath(os.path.dirname(__file__))
#
# #配置数据库路径
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(base_path,"orm.sqlite3")
# # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:WHDHX5301992@localhost/lou"
#
# #请求结束自动提交数据库操作
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# #flask1版本之后添加的跟踪修改
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SECRET_KEY"] = "123"
# #app加载数据库orm
# db = SQLAlchemy(app)
"""
包实例化文件
项目的实例化
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_restful import Api

bootstrap = Bootstrap()
api = Api()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DebugConfig")

    #惰性加载
    bootstrap.init_app(app)
    api.init_app(app)
    db.init_app(app)

    from Lou.blueprint import lou_app
    app.register_blueprint(lou_app)
#    app.register_blueprint(lou_app,url_prefix = "/louapp/")
    return app