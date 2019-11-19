"""
控制文件
"""
from flask_test.views import app

if __name__=='__main__':
    app.run(host="0.0.0.0",port = 8000,debug=True,use_reloader=True)