import smtplib
from email.mime.text import MIMEText

content = """
    祝愿第三阶段一切顺利！
"""
sender = "273116327@qq.com"
receiver = """
        1527473992@qq.com
        2276473611@qq.com

"""
password = "xgzqdhapzplpbgda"

#构建邮件格式
message = MIMEText(content,"plain","utf-8")
message["To"] = receiver
message["From"] = sender
message["Subject"] = "同桌的问候"

#发送邮件
smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,receiver.split(",\n"),message.as_string())
smtp.close()