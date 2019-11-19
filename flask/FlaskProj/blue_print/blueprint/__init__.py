from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blueprint.course import course

from blueprint.user import user

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    app.config.from_object("settings.DebugConfig")

    db.init_app(app)
    from blueprint.course import course
    from blueprint.user import user
    app.register_blueprint(course,url_prefix="/course/")
    app.register_blueprint(course,url_prefix="/user/")

    return app
