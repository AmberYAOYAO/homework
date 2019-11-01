from __future__ import absolute_import
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from Qshop.celery import app


@app.task
def add():
    x = 1
    y = 2
    return x+y
@app.task
def sendmail():
    #第三方SMTP服务
    from Qshop.settings import MAIL_PORT,MAIL_SENDER,MAIL_SERVER,MAIL_PASSWORD
    subject = '猜猜我是谁'
    content = "韦韦韦 MUA~"

    print(content)

#构建邮件格式
    message = MIMEText(content,"plain","utf-8")
    message["To"] = Header("1527473992@qq.com",'utf-8')
    message["From"] = Header(MAIL_SENDER,'utf-8')
    message["Subject"] = Header(subject,'utf-8')

#发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(MAIL_SERVER, 25)
    smtp.login(MAIL_SENDER,MAIL_PASSWORD)
    smtp.sendmail(MAIL_SENDER,"1527473992@qq.com",message.as_string())

