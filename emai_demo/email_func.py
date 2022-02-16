import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 创建邮箱服务器的连接
# 邮箱格式：smtp.test_wangxi@163.com
# 创建邮箱服务器的连接:分为SMTP，SMTP_SSL两种一种使用ssl加密，一种不用，邮箱连接时是通过addr+port的方式。
# 邮箱格式：smtp.test_wangxi@163.com
con=smtplib.SMTP_SSL('smtp.163.com','994')
# 登录时使用账号，密码/授权码来登录。
con.login(user='test_wangxi@163.com',password='NNAMSQXVGUWBTUGP')
# 发送者账号
sender='test_wangxi@163.com'
# 接受者账号
recevier=['302858210@qq.com','test_wangxi@163.com']
# 发送邮件
message=MIMEText(_text='邮件正文',_subtype='plain',_charset='utf-8')
message['Subject']=Header('文本标题嘻嘻嘻')
# 发件人
message['From']=Header('发件人wangxi','utf-8')
# 收件人
message['To']=Header('收件人copy_wangxi','utf-8')
# 发送邮件
con.sendmail(sender,recevier,message.as_string()) # message.as_string()是把正文转化为文本