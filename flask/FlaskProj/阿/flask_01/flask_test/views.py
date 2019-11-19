"""
视图文件
"""
from flask_test import app
from flask import render_template

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/new")
def new():
    return render_template("new.html")

# if __name__ == '__main__':
#     app.run(debug=True)
